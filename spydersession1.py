# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 19:04:58 2021

@author: Admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
superman = pd.read_csv('AAPL Historical Data.csv',usecols = [0,1,2,3,4])

POHL_avg = superman[['Price','Open','High','Low']].mean(axis = 1)

obs = np.arange(1,len(superman)+1,1)

plt.plot(obs,POHL_avg,'r',label= 'MY FIRST PLOT')