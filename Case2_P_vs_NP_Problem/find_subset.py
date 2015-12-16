from itertools import *
n = [-2,-3,15,14,7,-10]
return_set = []
def any_subset(n,p):
    for x in xrange(1,len(n) + 1):
        for i in combinations(n,x):
            if sum(i) == p:
                return_set.append(i)
    if return_set == []:
        print " No subset found"
    return return_set   
if __name__ == '__main__':     
    print any_subset(n,p = input('Enter subset value:  '))
