#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        if row == []:
            print("")
        else:
            for element in range(len(row)):
                if element == len(row) - 1:
                    print("{:d}".format(row[element]))
                else:
                    print("{:d}".format(row[element]), end=" ")
