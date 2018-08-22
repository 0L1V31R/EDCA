#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 10:50:52 2018

@author: lasea
"""

import numpy as np
from matplotlib import pyplot as plt
import sys
import time

def InsertionSort(A):
    for k in range(1, len(A)):
        pivo = A[k]
        i = k-1
        
        while (i >= 0) and pivo < A[i]:
            A[i+1] = A[i]
            i -= 1
        A[i + 1] = pivo
    return A

if __name__=="__main__":
    name = str(sys.argv[1])
    data = np.loadtxt(name)
    data = data[1:]
    t1 = time.clock()
    res = InsertionSort(data)
    t2 = time.clock()
    
    print(str(name) + ', tempo = {0:.8f}'.format(t2-t1))
    plt.figure()
    plt.plot(data, '.')
    plt.figure()
    plt.plot(res, '.')
    