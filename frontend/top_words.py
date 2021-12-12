import math
# from textblob import TextBlob as tb
from nltk import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')

def tf(word, blob):
    return blob.count(word) / len(blob)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


def calculate_top_words(doc1, doc2, doc3, doc4):

    result = []

    bloblist = [doc1, doc2, doc3, doc4]
    stop = set(stopwords.words('english'))

    for i, blob in enumerate(bloblist):
        # print("Top words in document {}".format(i + 1))
        data = [word for word in word_tokenize(blob.lower()) if word not in stop]

        scores = {word: tfidf(word, data, bloblist) for word in data}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        result.append(sorted_words[:3])

        # for word, score in sorted_words[:3]:
        #     print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

    return result


calculate_top_words("Please note that if we did find a problem, we would probably re-run all our regressions with an appropriate linr transformation. ", "What is your p-value for the heteroskedasticity test, and is it significant?", "Is the regression significant? How do you know?", "What is the slope coefficient for black? Is it statistically significant?")
