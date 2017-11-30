#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

#enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

pkl_file = (open("../final_project/final_project_dataset.pkl", "r"))

enron_data = pickle.load(pkl_file)

#print "Key list:\n", enron_data.keys()

#Q13
print "How many person in dataset? ", len(enron_data)
#Q14
print "For each penson, how many features are available? ", len(enron_data['FOY JOE'])

#Q15
cnt_poi = 0
for k in enron_data.keys():
    if enron_data[k]['poi'] == True:
        cnt_poi += 1
        print k, "is POI"

print"How many POIs in dataset?", cnt_poi
#Q18
print "what is the total value of the stock belonging to Prentice James?", enron_data['PRENTICE JAMES']['total_stock_value']
#Q19
print "How many messages do we have from Wesley Colwell to POIs?", enron_data['COLWELL WESLEY']['from_this_person_to_poi']
#Q20
print "what is value of stock options exercised by Skilling Jeffrey?", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

#Q25
max_payments = max(enron_data['LAY KENNETH L']['total_payments'],enron_data['SKILLING JEFFREY K']['total_payments'],enron_data['FASTOW ANDREW S']['total_payments'])
for k in ['LAY KENNETH L','SKILLING JEFFREY K','FASTOW ANDREW S']:
    if(enron_data[k]['total_payments'] == max_payments):
        name_of_max_pay = k
        break

print "Of Lay, Skilling and Fastow, who took home most money?"
print"It is", name_of_max_pay, ", he took", max_payments, "to home"

#Q27: 
