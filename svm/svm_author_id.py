#!/usr/bin/python
#-*-coding:utf-8-*-

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
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
from sklearn import svm
from sklearn import metrics
import numpy as np

# 将训练数据集切割到原来的1%, 丢掉99%的数据，再次测试training time and precision
def svm_clf_with_wholeTrainDataSet():
    # Create Classifier model
    clf = svm.SVC(kernel="linear")

    # Fit: load training datasets
    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 6),"s"

    # Predict:
    t0 = time()
    pred_result = clf.predict(features_test)
    print "predict time:", round(time()-t0,3),"s"

    #show the precision of new Classifier
    print(metrics.accuracy_score(labels_test,pred_result))

def svm_clf_with_miniTrainDataSet():
    features_train_min = features_train[:len(features_train)/100]
    labels_train_min = labels_train[:len(labels_train)/100]
    print "features_train_min len:",len(features_train_min),"labels_train_min len:",len(labels_train_min)

    # Create Classifier model
    clf = svm.SVC(kernel="linear")

    # Fit: load training datasets
    t0 = time()
    clf.fit(features_train_min, labels_train_min)
    print "training time:", round(time()-t0, 6),"s"

    # Predict:
    t0 = time()
    pred_result = clf.predict(features_test)
    print "predict time:", round(time()-t0,3),"s"

    #show the precision of new Classifier
    print "svm-linear accuracy:"
    print(metrics.accuracy_score(labels_test,pred_result))

def svm_clf_rbf(para_c):
    features_train_min = features_train
    labels_train_min = labels_train
    # features_train_min = features_train[:len(features_train)/100]
    # labels_train_min = labels_train[:len(labels_train)/100]
    #print "features_train_min len:",len(features_train_min),"labels_train_min len:",len(labels_train_min)
    print "features_train len:",len(features_train_min),"labels_train len:",len(labels_train_min)

    # Create Classifier model
    #para_c = 10000.
    clf = svm.SVC(kernel="rbf", C=para_c)
    print "SVC para c = ", para_c

    # Fit: load training datasets
    t0 = time()
    clf.fit(features_train_min, labels_train_min)
    print "training time:", round(time()-t0, 6),"s"

    # Predict:
    t0 = time()
    pred_result = clf.predict(features_test)
    print "predict time:", round(time()-t0,3),"s"

    #show the precision of new Classifier
    print "svm-rbf accuracy:"
    print(metrics.accuracy_score(labels_test,pred_result))

    print "pred[10] = ", pred_result[10]
    print "pred[26] = ", pred_result[26]
    print "pred[50] = ", pred_result[50]

    # print "now, predict the single test point:"
    #
    # pred = clf.predict(features_test[10])
    # print "predict features_test[10]:", pred
    #
    # pred = clf.predict(features_test[26])
    # print "predict features_test[26]:", pred
    #
    # pred = clf.predict(features_test[10])
    # print "predict features_test[50]:", pred

    print(metrics.classification_report(labels_test, pred_result, target_names={'chris','sara'}))

    email_num_chris = np.sum(pred_result==1)
    print "emails belong Chris is:", email_num_chris

    return clf
#########################################################
