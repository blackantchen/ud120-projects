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

# def DT_Classify(your_splite, features_train, labels_train):
#     clf = tree.DecisionTreeClassifier(min_samples_split=your_splite)
#     clf = clf.fit(features_train, labels_train)
#
#     return clf

# def check_dt_clf_accuracy(min_sample_split):
#     clf_min_samples_split = DT_Classify(min_sample_split, features_train, labels_train)
#     pred = clf_min_samples_split.predict(feature_test)
#
#     acc_min_sample_split = metrics.accuracy_score(labels_test, pred)
#     print("accuracy is ", acc_min_sample_split)


# clf_min_samples_split_2 = DT_Classify(2,features_train, labels_train)
#
# pred_2 = clf_min_samples_split_2.predict(features_test)
#
# acc_min_samples_split_2 = metrics.accuracy_score(labels_test, pred_2)

## min_samples_split = 50
#clf_min_samples_split_50 = DT_Classify(50, features_train, labels_train)
clf_min_samples_split_50 = tree.DecisionTreeClassifier(min_samples_split=50)
clf_min_samples_split_50 = clf_min_samples_split_50.fit(features_train, labels_train)

pred_50 = clf_min_samples_split_50.predict(features_test)

acc_min_samples_split_50 = metrics.accuracy_score(labels_test, pred_50)

print "acc_min_sample_split_50:", acc_min_samples_split_50

#########################################################
