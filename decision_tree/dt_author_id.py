#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
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
from sklearn import tree
from sklearn import metrics

def check_dt_clf_accuracy(your_splite):
    clf = tree.DecisionTreeClassifier(min_samples_split=your_splite)
    print"min_samples_split = ", your_splite

    t0 = time()
    clf = clf.fit(features_train, labels_train)
    print"training time:", round(time()-t0, 6),"s"

    t0 = time()
    pred = clf.predict(features_test)
    print"predict time:", round(time()-t0, 6),"s"

    acc_min_sample_split = metrics.accuracy_score(labels_test, pred)
    print"accuracy is ", acc_min_sample_split

print'number of features:', len(features_train[0])

check_dt_clf_accuracy(40)
#########################################################
