#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        for element in range(len(row)):
            print(row[element], end=" ")

        print()
