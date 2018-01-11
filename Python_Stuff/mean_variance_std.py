# Author:  Dorothy H. Sanchez
#
# This code will test for the Mean, Variance, and Standard Deviation of a sample set.
#
# Given a sample set with a Mean, then the variance of the sample is
# the sum of squares of the deviation from the mean divided by the sum of the elements of the sample.
#
# Test each data set one at a time

data1 =[13.04,1.32,22.65,17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
data2 = [2,5,7,9,12]
data3 = [1,3,7,10,14]
data4 = [7,9,12,15,20,33]
data5 = [6,8,10,12,14,16]
import math
def mean(data):
    return sum(data)/len(data)

def variance(data):
    sum_deviation = 0
    for i in data:
        deviation = math.pow((i - mean(data)),2) 
        sum_deviation += deviation
        answer = sum_deviation/len(data)
    return answer

def standard_dev(data):
    answer = round(math.sqrt(variance(data)),1)
    return answer

if __name__ == '__main__':
    print mean(data4)
    print variance(data4)
    print standard_dev(data4)
