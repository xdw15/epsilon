# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 01:51:16 2024

@author: P048168
"""

import numpy as np

import matplotlib.pyplot as plt


data=np.random.normal(0,1,[1000000,1])

plt.hist(data,bins=900)
