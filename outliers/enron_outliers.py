#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL', 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

# this was related to find an outlier that pops out in a graph...
# bad exercise.. is give a hint that the pdf from the final module would be useful
# but in reality, the problem was actually the TOTAL column
# ... really...
# despite I was pissed of, this kinda of Exploratory Data Analysis
# always leave a lot of useful functions and snippets behind... at quiz #18
# I get help from the below snippet

my_data = []

for item, features_dict in data_dict.items():
    if features_dict['salary'] != 'NaN' and features_dict['bonus'] != 'NaN':
        ratio = features_dict['bonus'] / float(features_dict['salary'])
        # print(item.rjust(30, ' ') + " => " + str(features_dict['salary']) + " \t\t " + str(features_dict['bonus']))
        my_data.append((item, features_dict['salary'], features_dict['bonus'], ratio))

my_data = sorted(my_data, key=lambda tup: tup[2])

for i in range(len(my_data)):
    print(str(my_data[i][0]).rjust(30, ' ') + " => " + str(my_data[i][1]) + " \t\t " + str(my_data[i][2]) + " \t\t " + str(my_data[i][3]))

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


