#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
import numpy as np
from sklearn import tree
from sklearn import metrics
from sklearn.cross_validation import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

poi_clf = tree.DecisionTreeClassifier()

poi_clf = poi_clf.fit(features_train, labels_train)

pred = poi_clf.predict(features_test)

accuracy = metrics.accuracy_score(labels_test, pred)

print"accuracy is ", accuracy

print "How many POIs are in test set ? ", np.sum(pred==1)
print "How many people total are in test set ? ", len(labels_test)
