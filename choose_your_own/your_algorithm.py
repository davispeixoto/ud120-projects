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
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.metrics import accuracy_score

# from sklearn.naive_bayes import GaussianNB
# algo = GaussianNB()
# name = 'naive_bayes'

# from sklearn.svm import SVC
# algo = SVC(C=10000)
# name = 'svc_c_10000'

# from sklearn.tree import DecisionTreeClassifier
# algo = DecisionTreeClassifier(criterion='entropy', min_samples_split=50)
# name = 'decision_tree_criterion_entropy_default_min_samples_50'

# from sklearn.neighbors import KNeighborsClassifier

# n_neighbors_list = [3, 5, 10, 20]
# weights_list = ['uniform', 'distance']
# algorithms_list = ['auto', 'ball_tree', 'kd_tree']

# from sklearn.ensemble import RandomForestClassifier

# n_estimators_list = [5, 10, 100, 1000]
# criterion_list = ['gini', 'entropy']
# min_samples_list = [2, 5, 10, 20, 50]

from sklearn.ensemble import AdaBoostClassifier
n_estimators_list = [5, 10, 50, 100]
learning_rate_list = [0.1, 0.5, 1.0]
algorithm_list = ['SAMME.R']

for i in range(len(n_estimators_list)):
    for j in range(len(learning_rate_list)):
        for k in range(len(algorithm_list)):
            n = n_estimators_list[i]
            lr = learning_rate_list[j]
            chosen_algo = algorithm_list[k]

            algo = AdaBoostClassifier(n_estimators=n, learning_rate=lr, algorithm=chosen_algo)
            name = 'ada_boost_n_estimators_' + str(n) + '_learning_rate_' + str(lr) + '_algo_' + chosen_algo

            clf = algo.fit(features_train, labels_train)
            pred =  clf.predict(features_test)

            accuracy = accuracy_score(labels_test, pred)
            print('n_estimators=' + str(n)  + ', learning_rate=' + str(lr)  + ', algorithm=' + chosen_algo)
            print(accuracy)
            print('---------------------------------------------')

            try:
                prettyPicture(clf, features_test, labels_test, name)
            except NameError:
                pass
