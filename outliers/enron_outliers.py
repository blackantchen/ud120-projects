#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

# take the biggest outliers point out
data_dict.pop("TOTAL", 0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
salary = []
bonus = []
for point in data:
    # salary = point[0]
    # bonus = point[1]
    salary.append(point[0])
    bonus.append(point[1])

matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

def find_keyName_from_dict(dictionary, bonus_value):
    outlier_keys = [0]
    for key in dictionary.keys():
        if dictionary[key]["bonus"] == bonus_value:
            outlier_keys.append(key)
            print 'key=',key,'bonus=',bonus_value,'salary=',dictionary[key]["salary"]

    # print "key of outlier is:", outlier_keys

    return outlier_keys

sorted_bonus = sorted(bonus, reverse=True)
print "the biggest outlier, bonus = ", sorted_bonus[:4]
sorted_salary = sorted(salary, reverse=True)
print "the most salary:", sorted_salary[:4]

# find the first 3 biggest bonus
find_keyName_from_dict(data_dict, sorted_bonus[0])
find_keyName_from_dict(data_dict, sorted_bonus[1])
find_keyName_from_dict(data_dict, sorted_bonus[2])
