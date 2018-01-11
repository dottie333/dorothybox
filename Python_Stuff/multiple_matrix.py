# -*- coding: utf-8 -*-
"""
Created on Thu Jul 03 21:49:48 2014

@author: Dorothy H. Sanchez
"""

import numpy as np

def multiple_matrix():
    a = np.matrix([[2,3],[4,7]])
    b = np.matrix([[1,2],[4,3]])
    
    answer = a * b
    return answer
    
if __name__ == '__main__':
    print multiple_matrix()

# note:  ab does not equal ba