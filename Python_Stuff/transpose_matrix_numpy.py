# -*- coding: utf-8 -*-
"""
Created on Thu Jul 03 23:03:56 2014

@author: Dorothy H. Sanchez
"""

from numpy import matrix
def transpose_matrix(data):
    
    data = matrix(data)
    
    return data.T

if __name__ == '__main__':
    
    print transpose_matrix([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]]) 
    print transpose_matrix([[1, 4, 3],
                          [8, 2, 6],
                          [7, 8, 3],
                          [4, 9, 6],
                          [7, 8, 1]])


