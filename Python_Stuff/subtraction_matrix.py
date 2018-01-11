# -*- coding: utf-8 -*-
"""
Created on Thu Jul 03 21:49:48 2014

@author: Dorothy H. Sanchez
"""

import numpy as np
def subtraction_matrix():
    a = np.matrix([[3,4],[2,1]])
    b = np.matrix([[6,8],[2,3]])
    
    answer = a - b
    return answer
    
if __name__ == '__main__':
    print subtraction_matrix()

