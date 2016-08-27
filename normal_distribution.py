# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 16:30:02 2016

@author: liyu.li
"""

from scipy import stats
import numpy as np
x = np.linspace(-15, 15, 9)
if stats.kstest(x,"norm")[1]<0.05:
    print ("x is not drawn from the normal distribution,不服从正太分布")
else:
    print( "x is  drawn from the normal distributio 服从正太分布n")
print("end")
print("end")