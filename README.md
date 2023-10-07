# Introduction
 A simple introduction to statistical learning in time-series forecasting. This package enables you to build, train and test a time-series forcasting model using Exponential Smoothing techniques. Learn more here: https://machinelearningmastery.com/exponential-smoothing-for-time-series-forecasting-in-python/ 

# Usage 
Download and run the package on your local system. Python version 3.10 or greater is advised.

# Model 
Simple Exponential Smoothing can be interpreted as a weighted average of the time-series values, wherein the weights are either exponentially increasing (greater importance to future values in the time-series) or exponentially decreasing (greater importance to earlier values in the time-series). The "alpha" value or the smoothing parameter lies between 0 and 1 - the greater the value of alpha, the greater is the exponentially increasing nature of the weights.

# Error metrics 
In order to train the model, one can choose from the following error metrics to minimize in order to obtain the optimal "alpha" value: 

![image](https://github.com/akomarla/ExpSmoothing/assets/124313756/15ee78b6-024c-4f49-b730-2d40dba3fb46)

# Questions
Contact aparna.komarla@gmail.com with any questions.

