#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

# Adaboost classifier
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics
from sklearn import svm
from time import time

def svm_clf_rbf():
    features_train_min = features_train
    labels_train_min = labels_train
    print "features_train len:",len(features_train_min),"labels_train len:",len(labels_train_min)

    # Create Classifier model
    para_c = 10000.
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

    return clf

clf = svm_clf_rbf()

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
