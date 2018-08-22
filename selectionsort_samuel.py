#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 15:57:04 2018

@author: lasea
"""

import numpy as np
import sys
import time

def SelectionSort(A):
    for i in range(1,len(A)):
        iMin = i
        for j in range(i+1, len(A)):
            if A[j] < A[iMin]:
                iMin = j
        if A[i] != A[iMin]:
            temp = A[i]
            A[i] = A[iMin]
            A[iMin] = temp
    return A

if __name__=="__main__":
    name = str(sys.argv[1])
    data = np.loadtxt(name)
    data = data[1:]
    t1 = time.clock()
    res = SelectionSort(data)
    t2 = time.clock()
    
    print(str(name) + ', tempo = {0:.8f}'.format(t2-t1))