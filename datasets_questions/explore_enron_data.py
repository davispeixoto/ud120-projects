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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# people = len(enron_data)
# print(people)

#person, features_dict = enron_data.items()[0]

#print(person)
#for feature, value in features_dict.items():
#    print(feature + ' => ' + str(value))

# people_on_poi = [ person for person, features_dict in enron_data.items() if features_dict["poi"] == True]
# print(len(people_on_poi))

# print(enron_data['PRENTICE JAMES']['total_stock_value'])
# print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
# print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

#for i in enron_data.keys():
#    print(i)

#ken_payment = enron_data['LAY KENNETH L']['total_payments']
#andy_payment = enron_data['FASTOW ANDREW S']['total_payments']
#jeff_payment = enron_data['SKILLING JEFFREY K']['total_payments']

#print(ken_payment)
#print(andy_payment)
#print(jeff_payment)

no_salary = [person for person, features_dict in enron_data.items() if features_dict['salary'] == 'NaN']
print(len(enron_data) - len(no_salary))

