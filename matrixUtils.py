#!/usr/bin/env python3
import argparse
import numpy as np
import time

def genMatrix(size, value):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = [[value for col in range(0,size)] for row in range(0,size)]

    return matrix

def genMatrix2(size, value):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = np.asarray([ np.asarray([value for col in range(0,size)]) for row in range(0,size)])

    return matrix

def printSubarray(matrix, size=10):
    """
    Prints the upper left subarray of dimensions size x size of
    the matrix
    """

    for row in range(1, 10):
        for col in range(1, 10):
            print(f'{matrix[row][col]}' , end='')
        print('')

def writeToFile(matrix, fileName):
    """
    Writes a matrix out to a file
    """

    with open(fileName, 'w') as file:
        for row in matrix:
            for col in row:
                file.write(f'{col} ')
            file.write('\n')

def readFromFile(fileName):
    """
    Reads a matrix from a file
    """

    matrix = []

    with open(fileName, 'r') as file:
        for line in file:
            row = [int(val) for val in line.split()]
            matrix.append(row)

    return matrix

def matrixMult(m1, m2):
    matrix = genMatrix2(512, 0)
    for x in range(len(m1)):
        for y in range(len(m2[0])):
            for k in range (len(m2)):
                matrix[x][y] = (m1[x][k]) * (m2[k][y])
    return matrix

def matrixBlocked(m1, m2):
    length = len(m1)
    matrix = genMatrix(length, 0)
    tile_size = 16

    for kk in range(0, length, tile_size):
        for jj in range(0, length, tile_size):
            for i in range(0, length):
                j_end = jj + tile_size
                for j in range (jj, j_end):
                    k_end = kk + tile_size
                    sum = matrix[i][j]
                    for k in range (kk, k_end):
                        sum = m1[i][k]*m2[k][j]
                    matrix[i][j] = sum
    return matrix

def main():
    """
    Used for running as a script
    """
    size = int(input("Enter the size of the matrix: "))
    if size < 10: size = 10
    val1 = int(input("Enter the value of first array: "))
    val2 = int(input("Enter the value of second array: "))

    m1 = genMatrix(size, val1)
    m2 = genMatrix(size, val2)

    start = time.monotonic()
    mat3 = matrixMult(m1, m2)
    time1 = time.monotonic() - start

    start = time.monotonic()
    mat3 = matrixBlocked(m1, m2)
    time2 = time.monotonic() - start

    printSubarray(mat3)
    print("Matrix multiply time: %s seconds" % time1)
    print("Blocked time: %s seconds" % time2)
if __name__ == '__main__':
    # execute only if run as a script
    main()
