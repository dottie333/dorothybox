# Author:  Dorothy H. Sanchez
#
# This function will remove duplicate values from a list
#
def remove_duplicates(x):
    new_list = []
    for i in x:
        if i in new_list:
            pass
        else:
            new_list.append(i)
            
    return new_list

if __name__ == '__main__':
    print remove_duplicates([1,1,2,2,2,3,4,4,4,5,8])
