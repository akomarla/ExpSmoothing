# Introduction
 A simple introduction to statistical learning in time-series forecasting. This package enables you to build, train and test a time-series forcasting model using the Simple Exponential Smoothing method. Learn more here: https://machinelearningmastery.com/exponential-smoothing-for-time-series-forecasting-in-python/ 

# Usage 
Download and run the package on your local system. Python version 3.10.0 or greater is advised.

# Model 
Simple Exponential Smoothing can be interpreted as a weighted average of the time-series values, wherein the weights are either exponentially increasing (greater importance to future values in the time-series) or exponentially decreasing (greater importance to earlier values in the time-series). The "alpha" value or the smoothing parameter lies between 0 and 1: the greater the value of alpha, the greater is the exponentially increasing nature of the weights.

## Error metrics 
Simply put, training the model involves finding the "alpha" value that minimizes the error (difference between true and forecasted values). In this implementation, one can choose from the following error metrics to obtain the optimal "alpha" value: 

![image](https://github.com/akomarla/ExpSmoothing/assets/124313756/15ee78b6-024c-4f49-b730-2d40dba3fb46)

## Implementation 
This model is trained and tested on the M4 dataset of the Makridakis Time-Series Forecasting Competition: https://github.com/Mcompetitions/M4-methods/tree/master/Dataset (Daily-train.csv and Daily-test.csv) using the mean absolute percentage error metric from the table above. 

# Questions
Contact aparna.komarla@gmail.com with any questions.

