#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
from sklearn.tree import DecisionTreeClassifier

regressor = DecisionTreeClassifier()
regressor.fit(features_train, labels_train)
print(regressor.score(features_test, labels_test))

# bigger = 0
# index = 0
#
# for i in range(len(regressor.feature_importances_)):
#     if regressor.feature_importances_[i] > bigger:
#         bigger = regressor.feature_importances_[i]
#         index = i
#
# print(bigger)
# print(index)

outliers = []
threshold = 0.2
index = 0

for i in range(len(regressor.feature_importances_)):
    if regressor.feature_importances_[i] > threshold:
        index = i
        print(i)
        print(regressor.feature_importances_[i])
        print('----')

# features_importances_filtered = [feature for feature in regressor.feature_importances_ if feature > 0.2]
# features_importances_sorted = sorted(features_importances_filtered)
# # print(features_importances_sorted.pop())

features = vectorizer.get_feature_names()
print(features[index])
