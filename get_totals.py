# Author:  Dorothy H. Sanchez
#
# This function will return the total of elements in a list

def add_numbers():
    numbers = [2,3,4,8,9,22,33,65]
    return 'The total is', get_total(numbers)

def get_total(value_list):
    total = 0
    for num in value_list:
        total += num
    return total

if __name__ == '__main__':
    print add_numbers()
