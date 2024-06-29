# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 01:51:16 2024

@author: P048168
"""

import numpy as np

import matplotlib.pyplot as plt


data_1=np.random.normal(0,1,[1000000,1])

data_2=np.random.normal(0,1,[1000000,1])

#plt.hist(data,bins=900)

plt.scatter(data_1,data_2)
