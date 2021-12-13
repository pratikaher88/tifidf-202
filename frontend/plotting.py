# from sklearn.feature_extraction.text import TfidfVectorizer
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# def get_plotted_image():
#     tfidf_vectorizer = TfidfVectorizer(stop_words='english')
#     tfidf_feature = tfidf_vectorizer.fit_transform([
#                                                        "Please note that if we did find a problem, we would probably re-run all our regressions with an appropriate linr transformation. ",
#                                                        "What is your p-value for the heteroskedasticity test, and is it significant?",
#                                                        "Is the regression significant? How do you know?",
#                                                        "What is the slope coefficient for black? Is it statistically significant?"])
#
#     tfidf_dataframe = pd.DataFrame(data=tfidf_feature.todense(), columns=tfidf_vectorizer.get_feature_names())
#     tfidf_dataframe = tfidf_dataframe.T
#
#     # Computing the correlation matrix
#     X_corr = tfidf_dataframe.corr()
#
#     # Computing eigen values and eigen vectors
#     values, vectors = np.linalg.eig(X_corr)
#
#     # Sorting the eigen vectors coresponding to eigen values in descending order
#     args = (-values).argsort()
#     values = vectors[args]
#     vectors = vectors[:, args]
#
#     # Taking first 2 components which explain maximum variance for projecting
#     new_vectors = vectors[:, :2]
#
#     # Projecting it onto new dimesion with 2 axis
#     neww_X = np.dot(X, new_vectors)
#
#     plt.figure(figsize=(13, 7))
#     # plt.scatter(neww_X[:,0],neww_X[:,1],linewidths=10,color='blue')
#     plt.xlabel("PC1", size=15)
#     plt.ylabel("PC2", size=15)
#     plt.title("Word Embedding Space", size=20)
#     vocab = list(tfidf_vectorizer.get_feature_names())
#     for i, word in enumerate(vocab):
#         plt.scatter(neww_X[i, 0], neww_X[i, 1], linewidths=10, color='blue')
#         plt.annotate(word, xy=(neww_X[i, 0], neww_X[i, 1]))
