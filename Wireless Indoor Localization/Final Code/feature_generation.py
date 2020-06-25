# -*- coding: utf-8 -*-
"""Feature_generation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J5VI8UIm-5BlCCbm8ZJg3zi5lU9WLy5t
"""

import pandas as pd
import numpy as np

#Introducing new features as nonlinear functions of the given features(nonlinear mapping)
"""
    This function generates features with regard to physical meaning of the features like mean 
    and standard deviation of the signal power, minimum and maximum values of signal power and scaling.
"""

def get_features(X):
    for key in X.columns:
        X[key] = 10 ** (X[key]/20)
    X['mean'] = X.mean(axis=1)
    X['std'] = X.std(axis=1)
    for key in X.columns:
        X[key] = 20*(np.log10(X[key]))                                            #Citation - scipy.org numpy documentation
    for key in X.columns:
        if key not in ['mean', 'std']:
            X[key+'_scaled'] = (X[key] - X['mean']) / X['std']
    X['Max_WS'] = X[['WS1', 'WS2', 'WS3', 'WS4', 'WS5', 'WS6', 'WS7']].idxmax(axis = 1)
    X['Min_WS'] = X[['WS1', 'WS2', 'WS3', 'WS4', 'WS5', 'WS6', 'WS7']].idxmin(axis=1)
    X['Min_Max'] = X['Max_WS'] + X['Min_WS']
    max_ws_df = X.groupby('Max_WS').mean().reset_index()
    X = X.merge(max_ws_df, on = 'Max_WS', suffixes=('', '_max_ws'), how = 'left')
    for key in X.columns:
        if '_max_ws' in key:
            X[key+'_dist'] = np.fabs(X[key] - X[key[:-len('_max_ws')]])           #Citation - scipy.org numpy documentation
    min_ws_df = X.groupby('Min_WS').mean().reset_index()
    X = X.merge(min_ws_df, on = 'Min_WS', suffixes=('', '_min_ws'), how = 'left')
    for key in X.columns:
        if '_min_ws' in key:
            X[key+'_dist'] = np.fabs(X[key] - X[key[:-len('_min_ws')]])            #Citation - scipy.org numpy documentation
    min_ws_df = X.groupby('Min_Max').mean().reset_index()
    X = X.merge(min_ws_df, on = 'Min_Max', suffixes=('', '_min_max'), how = 'left')
    for key in X.columns:
        if '_min_max' in key:
            X[key+'_dist'] = np.fabs(X[key] - X[key[:-len('_min_max')]])
    return pd.get_dummies(X)                                                           #Citation - pandas API reference documentation