# -*- coding: utf-8 -*-
"""
Created on Thu Jul 03 21:49:48 2014

@author: Dorothy H. Sanchez
"""

import numpy as np
def add_matrix():
    a = np.matrix([[3,3],[1,2]])
    b = np.matrix([[3,4],[5,6]])
    
    answer = a + b
    return answer
    
if __name__ == '__main__':
    print add_matrix()

