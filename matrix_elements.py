# Author:  Dorothy H. Sanchez
#
# This will list all elements of a matrix.

def matrix_elements():
    matrix = [[5,4,3,2],[6,4,5,3]]
    row = 0
    while row <= len(matrix) -1:
        col = 0
        while col <= len(matrix[0]) -1:
            print matrix[row][col]
            col += 1
        row += 1

matrix_elements()
        
