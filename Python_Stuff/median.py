# -*- coding: utf-8 -*-
"""
Created on Wed Jul 02 00:58:01 2014

@author: Dorothy H. Sanchez
"""
# This will give you median of a sample set

def find_median(data):
    data = sorted(data)
    
    middle_point = len(data)/2
    
    if len(data) % 2 != 0:
        return data[middle_point]
    else:
        return(data[middle_point] + data[middle_point - 1]) /2.0
        
if __name__ == '__main__':
    print find_median([5,8,3,6,9,4,10])
    print find_median([3,6,4,7,8,9]) 
    print find_median([4,5,6,6,6,7,7,8])
    print find_median([2,3,4,5,5,6,7,7,10])

    
