import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from num2words import num2words

import nltk
import os
import string
import numpy as np
import copy
import pandas as pd
import pickle
import re
import math

def convert_lower_case(data):
    return np.char.lower(data)

def remove_punctuation(data):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
        data = np.char.replace(data, "  ", " ")
    data = np.char.replace(data, ',', '')
    return data

def remove_apostrophe(data):
    return np.char.replace(data, "'", "")


def stemming(data):
    stemmer = PorterStemmer()

    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return new_text

def convert_numbers(data):
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        try:
            w = num2words(int(w))
        except:
            a = 0
        new_text = new_text + " " + w
    new_text = np.char.replace(new_text, "-", " ")
    return new_text

def remove_stop_words(data):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text



def preprocess(data):
    data = convert_lower_case(data)
    data = remove_punctuation(data) #remove comma seperately
    data = remove_apostrophe(data)
    data = remove_stop_words(data)
    data = convert_numbers(data)
    data = stemming(data)
    data = remove_punctuation(data)
    data = convert_numbers(data)
    data = stemming(data) #needed again as we need to stem the words
    data = remove_punctuation(data) #needed again as num2word is giving few hypens and commas fourty-one
    data = remove_stop_words(data) #needed again as num2word is giving stop words 101 - one hundred and one
    return data




def calculate_scores(doc1, doc2, doc3, doc4):

    processed_text = []
    # processed_title = []

    processed_text.append(word_tokenize(str(preprocess(doc1))))
    processed_text.append(word_tokenize(str(preprocess(doc2))))
    processed_text.append(word_tokenize(str(preprocess(doc3))))
    processed_text.append(word_tokenize(str(preprocess(doc4))))

    # print(processed_text)

    DF = {}

    for i in range(4):
        tokens = processed_text[i]
        for w in tokens:
            try:
                DF[w].add(i)
            except:
                DF[w] = {i}

    for i in DF:
        DF[i] = len(DF[i])

    doc = 0
    tf_idf = {}
    for i in range(4):
        tokens = processed_text[i]
        counter = Counter(processed_text[i])
        words_count = len(tokens)

        for token in np.unique(tokens):
            tf = counter[token] / words_count
            df = 0
            try:
                df = DF[token]
            except:
                pass

            idf = np.log(4 / (df + 1))
            tf_idf[doc, token] = tf * idf

    print(tf_idf)

    # for i in tf_idf:
    #     tf_idf[i] *= alpha

    pass


calculate_scores("Please note that if we did find a problem, we would probably re-run all our regressions with an appropriate linr transformation. ", "What is your p-value for the heteroskedasticity test, and is it significant?", "Is the regression significant? How do you know?", "What is the slope coefficient for black? Is it statistically significant?")
