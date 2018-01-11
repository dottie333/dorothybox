# Author:  Dorothy H. Sanchez
#
# This function will remove odd numbers from a list

def odd_numbers(x):
    return [number for number in x if number %2 == 0]

if __name__ == '__main__':

    print odd_numbers([1,2,3,4,5,6,7,8,9,11])
