# -*- coding: utf-8 -*-
"""Feature_selection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mkmMpiX6oxOx-SwtJv6TlO_-4XbO0Zg1
"""

#!pip install -U yellowbrick                                              #Citation - pypi.org yellowbrick documentation

import pandas as pd
from feature_generation import get_features
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
from yellowbrick.model_selection import FeatureImportances
import xgboost
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Read Training data
df = pd.read_csv('D_Train1.csv')                                                   #Citation - pandas API reference documentation
X = df.drop(columns = ['Location'])
y = df['Location']

X = get_features(X)

X.shape

#Fill NA/NaN values
X.fillna(0, inplace=True)                                                          #Citation - pandas API reference documentation

#Feature ranking with recursive feature elimination.
estimator = xgboost.XGBClassifier(tree_method = 'gpu_hist')                       #Citation - xgboost.readthedocs.io xgboost API reference documentation
selector = RFE(estimator, verbose = 0, n_features_to_select = 40)                 #Citation - scikit-learn.org sklearn API reference documentation

selector.fit(X, y)

#Select the best features 
selected = [X.columns[i] for i in selector.get_support(indices=True)]             #Citation - scikit-learn.org sklearn API reference documentation

selected

X = X[selected]

plt.figure(figsize=(11,9))
ax = plt.gca()                                                                    #Citation - from matplotlib.org matplotlip API reference documentation

# Title case the feature for better display and create the visualizer
model = RandomForestClassifier(n_jobs = -1)                                       #Citation - scikit-learn.org sklearn API reference documentation
labels = list(map(lambda s: s.title(), X.columns))  
viz = FeatureImportances(model, labels=labels, relative=True)                     #Citation - scikit-yb.org yellowbrick documentation 

# Fit and show the feature importances
viz.fit(X, y)
viz.show(ax=ax)