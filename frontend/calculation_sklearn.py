from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


def calculate_scores(doc1, doc2, doc3, doc4):

 tfidf_vectorizer = TfidfVectorizer(stop_words = 'english',smooth_idf = True, token_pattern=r'(?u)\b[A-Za-z]+\b')

 doc_list = []
 if doc1:
  doc_list.append(doc1)
 if doc2:
  doc_list.append(doc2)
 if doc3:
  doc_list.append(doc3)
 if doc4:
  doc_list.append(doc4)

 tfidf_feature = tfidf_vectorizer.fit_transform(doc_list)

 tfidf_dataframe = pd.DataFrame(data=tfidf_feature.todense(), columns=tfidf_vectorizer.get_feature_names_out())

 words = tfidf_dataframe.columns.tolist()

 # print(tfidf_dataframe)

 tfidf_dataframe = tfidf_dataframe.transpose()
 # print(dataframe.iloc[0])

 tfidf_dataframe = tfidf_dataframe.assign(max_value=(tfidf_dataframe.idxmax(axis=1)+1))

 return [(i, j) for i, j in zip(words, tfidf_dataframe.values.tolist())]
 # print(vectorizer.get_feature_names_out())
 # print(X.shape)




# calculate_scores("Please note that if we did find a problem, we would probably re-run all our regressions with an appropriate linr transformation. ", "What is your p-value for the heteroskedasticity test, and is it significant?", "Is the regression significant? How do you know?", "What is the slope coefficient for black? Is it statistically significant?")
