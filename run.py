# -*- coding: utf-8 -*-

from model import *
import pandas as pd
import numpy as np
import logging
import os
import pyodbc as po
from datetime import datetime
from tqdm import tqdm
import copy
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing, Holt
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split
from scipy import stats

##############################################################################################################################################################

# Getting training time series from M4 forecasting competition training set
url = 'https://raw.githubusercontent.com/Mcompetitions/M4-methods/master/Dataset/Train/Daily-train.csv'
# Get training data as dataframes
raw = pd.read_csv(url)
cols = ['V'+str(i) for i in range(2,401)]
train = raw[cols]
train_true = raw['V401']
# Convert to correct data type to run the model 
train = train.values.tolist()
train_true = [[val] for val in train_true.tolist()]

# Getting testing time series from M4 forecasting competition testing set
url = 'https://raw.githubusercontent.com/Mcompetitions/M4-methods/master/Dataset/Train/Daily-train.csv'
# Get testing data as dataframes
raw = pd.read_csv(url)
cols = ['V'+str(i) for i in range(2,401)]
test = raw[cols]
test_true = raw['V401']
# Convert to correct data type to run the model 
test = test.values.tolist()
test_true = [[val] for val in test_true.tolist()]

###############################################################################

# Train the exponential smoothing model - learn the best alpha parameter by minimizing the mean abs % error
es = ExpSmoothing()
es.train(train_data = train, 
         train_true_values = train_true, 
         error = 'mean absolute percentage error', 
         num_gen = 1, 
         remove_outliers = False, 
         non_neg = False, 
         non_zero = False)
# Test the model
ft, error = es.test(test_data = test, 
                    test_true_values = test_true, 
                    remove_outliers = False, 
                    non_neg = False, 
                    non_zero = False)

# Print model results
print('Model results')
print('Best smoothing parameter (alpha):', es.param['alpha'])
print('Error used for training:', es.error)
print('Training error:', es.train_error)
print('Testing error:', es.test_error)

###############################################################################

# Analyze and predict future values
ft = pd.DataFrame()

ft_avg_non_neg = []
ft_avg = []
ft_exp_smooth = []
for t in test:
    ts = Analyze(values = t, labels = None)
    # Find average of non-negative values only
    ft_avg_non_neg.append(ts.forecast(how = 'average non-neg'))
    # Find average of all values only
    ft_avg.append(ts.forecast(how = 'average'))
    # Find exponential smoothing forecast using parameter learned from training
    ft_exp_smooth.append(ts.forecast(how = 'exponential smoothing', param = es.param, num_gen = 1)[0][0])

# Adding true values to the df
ft['true'] = [val[0] for val in test_true]

# Add columns with forecast and difference b/w true and forecasted values
ft['Average non-neg'] = ft_avg_non_neg
ft['Average non-neg (diff)'] = ft['true'] - ft['Average non-neg']

ft['Average'] = ft_avg
ft['Average (diff)'] = ft['true'] - ft['Average']

ft['Exponential smoothing forecast'] = ft_exp_smooth
ft['Exponential smoothing forecast (diff)'] = ft['true'] - ft['Exponential smoothing forecast']

# Write results to Excel
ft.to_excel('...data/results/forecasts.xlsx')

###############################################################################
  