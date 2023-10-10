# Introduction
 A simple introduction to statistical learning in time-series forecasting. This model is a lightweight and easy to understand example of model traning, testing and implementation. The package enables one to build, train and test a time-series forcasting model using the Simple Exponential Smoothing method. 

Learn more here: https://machinelearningmastery.com/exponential-smoothing-for-time-series-forecasting-in-python/ 

# Usage 
Download and run the package on your local system. Python version 3.10.0 or greater is advised.

# Model 
Simple Exponential Smoothing can be interpreted as a weighted average of the time-series values, wherein the weights are either exponentially increasing (greater importance to future values in the time-series) or exponentially decreasing (greater importance to earlier values in the time-series). The "alpha" value or the smoothing parameter lies between 0 and 1: the greater the value of alpha, the greater is the exponentially increasing nature of the weights.

<img src= "https://github.com/akomarla/ExpSmoothing/assets/124313756/5f638da2-6b86-4714-87b0-3b466f893115" width = "40%" height = "40%">

Learn more here: https://btsa.medium.com/introduction-to-exponential-smoothing-9c2d5909a714

## Error metrics 
Simply put, training the model involves finding the "alpha" value that minimizes the forecast error (difference between true and forecasted values). In this implementation, one can choose from the following error metrics to obtain the optimal "alpha" value:
| Error | Parameter | Formula | More information |
| ------------ | -------------- | --------- |--------- |
| Mean Squared Error (MSE) | ```mean squared error``` | <img src = "https://github.com/akomarla/ExpSmoothing/assets/124313756/a58bc3d7-6661-4995-825d-b031bd62016a" width = "80%" height = "80%"> | https://en.wikipedia.org/wiki/Mean_squared_error |
| Root Mean Squared Error (RMSE) | ```root mean squared error``` | <img src = "https://github.com/akomarla/ExpSmoothing/assets/124313756/13106816-f256-4e74-ad06-b20470cc6f74" width = "80%" height = "80%"> | https://towardsdatascience.com/what-does-rmse-really-mean-806b65f2e48e |
| Mean Absolute Error (MAE) | ```mean absolute error``` | <img src = "https://github.com/akomarla/ExpSmoothing/assets/124313756/a5821e63-0020-4fa2-aea7-993ba6c6babe" width = "80%" height = "80%"> | https://en.wikipedia.org/wiki/Mean_absolute_error |
| Mean Absolute Percentage Error (MAPE) | ```mean absolute percentage error``` | <img src = "https://github.com/akomarla/ExpSmoothing/assets/124313756/4825f7e2-f0c6-4396-b27f-2333542f2d84" width = "80%" height = "80%"> | https://en.wikipedia.org/wiki/Mean_absolute_error |


Where n represents the number of time-series in the data set, and e is the difference between the true and forecasted values for a particular time series. 

## Implementation 
This model is trained and tested on the M4 dataset of the Makridakis Time-Series Forecasting Competition: https://github.com/Mcompetitions/M4-methods/tree/master/Dataset (Daily-train.csv and Daily-test.csv) using the mean absolute percentage error metric from the table above. 

# Questions
Contact aparna.komarla@gmail.com with any questions.

