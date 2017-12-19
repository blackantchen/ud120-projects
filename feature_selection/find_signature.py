#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
from sklearn import tree
from sklearn import metrics

# create classifier
clf = tree.DecisionTreeClassifier(min_samples_split = 40)

print "number of train data points:", len(features_train)
clf = clf.fit(features_train, labels_train)

test_pred = clf.predict(features_test)

accuracy_test = metrics.accuracy_score(labels_test, test_pred)
print "accuracy_score of test datasets:", accuracy_test

f_id = 0
most_w = 0
most_f_id = 0
feature_names_list = vectorizer.get_feature_names()

for w in clf.feature_importances_:
    if w > 0.2:
        print "feature weight:", w, "index:", f_id, "name:", feature_names_list[f_id]
        if w > most_w:
            most_w = w
            most_f_id = f_id

    f_id += 1

print "the most import feature is:", most_w, "Num:", most_f_id
print "Name of the most import feature:", feature_names_list[most_f_id]
