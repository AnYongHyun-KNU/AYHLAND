# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:22:53 2019

@author: pc
"""

import numpy as np

a= np.zeros((256,3),np.int32) # 괄호좀 빼먹지마라 행렬 차원 
b = np.zeros((3,256),np.int32)
a1=a[:,0]
b1=b[0,:]

print(a1.shape) # (256,)
print(b1.shape) #