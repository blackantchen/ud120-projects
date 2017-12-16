#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle
import cPickle
import numpy as np

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

### the authors and words already be save in "your_email_authors.pkl"
### "your_word_data.pkl" by vectorize_text.py
authors_file_handler = open("your_email_authors.pkl","r")
authors = pickle.load(authors_file_handler)
authors_file_handler.close()

words_file_handler = open("your_word_data.pkl", "r")
words_data = cPickle.load(words_file_handler)
words_file_handler.close()

# sw = stopwords.words("english")

# vectorizer = TfidfVectorizer(stop_words=sw)
vectorizer = TfidfVectorizer(stop_words="english") # 注意不要引用nltk创建的stop_words,否则会得到不一样的结果，暂时不解

words_data_vectorize = vectorizer.fit_transform(words_data)

print "words_data shape:", words_data_vectorize.shape

feature_name_list = vectorizer.get_feature_names()
# print "feature names:", feature_name_list
print "length of feature_names:", len(feature_name_list)
print "word 34597 in TfIdf Matrix:", feature_name_list[34597]
