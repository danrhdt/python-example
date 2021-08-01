# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 13:21:20 2021

@author: DAN-HDT
"""

import numpy as np

A=np.loadtxt('sample.txt',delimiter=' ')
B=A[:,1:2]
np.savetxt('samp.txt',B,fmt='%.2f',delimiter=' ')
print(B)