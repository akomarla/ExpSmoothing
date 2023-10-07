# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 18:43:53 2023

@author: akomarla
"""

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