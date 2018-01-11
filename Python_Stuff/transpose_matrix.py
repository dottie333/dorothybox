# Author:  Dorothy H. Sanchez
# This code build will create the transpose of a matrix

def transpose_matrix(data):
    items= []
    new_matrix = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]

    for x in new_matrix:
        #print x
        items.append(x)
    return items


if __name__ == '__main__':
    print transpose_matrix([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]]) 
    assert transpose_matrix([[1, 4, 3],
                           [8, 2, 6],
                           [7, 8, 3],
                           [4, 9, 6],
                           [7, 8, 1]])


