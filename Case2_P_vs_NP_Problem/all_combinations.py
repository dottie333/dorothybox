from itertools import *
from math import factorial
n = [-2,-3,15,14,7,-10]
# This provides all the possible combinations(subsets)
# of the dataset given and the total for each subset.
def find_answerset(n):
    no_return = ''
    count_combinations = 0
    each_element_in_set = 0
    print 'Given a data set of size', len(n)
    print 'this report will give you a list of all the possible subsets'
    print
    for x in xrange(1,len(n) + 1):
        each_element_in_set += 1
        print 'The total combinations of',x, 'element subset:', factorial(len(n))  /  (factorial(x) * factorial(len(n) - x))
        for i in combinations(n,x):
            count_combinations += 1
            print count_combinations,'\t', each_element_in_set,'\t',i,'\t'," Total:",'  ', sum(i)
    return no_return
if __name__ == '__main__':
    print find_answerset(n)
