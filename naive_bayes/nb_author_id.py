#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

t0 = time()
# Build Classifier and load datasets into
clf = MultinomialNB().fit(features_train, labels_train)
print "training time:", round(time()-t0,3),"s"

t0 = time()
# use new Classifier to class test datasets
pred = clf.predict(features_test)
print "predict time:", round(time()-t0,3),"s"

# show the precision
#show the precision of new Classifier
print "naive-bayes accuracy:"
print(metrics.accuracy_score(labels_test, pred))

# expect_y = labels_test
# print(metrics.classification_report(expect_y, test_classed, target_names={'chris','sara'}))

#########################################################
