#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        pass
    ln = len(matrix)
    for x in range(ln):
        for y in range(len(matrix[x])):
            print('{:d}'.format(matrix[x][y]), end='')
            if y is not (len(matrix[x]) - 1):
                print(end=" ")
        print("")
