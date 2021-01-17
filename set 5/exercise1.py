#!/usr/bin/env python
import os

def squareRootMat(matrix):
    return [[m ** 0.5 for m in row] for row in matrix]

if __name__ == "__main__":
    A = [[1,2,3,4], [2,25,35,45], [7,3,17,27], [8,9,21,30]]

    file = open('MatFile.txt','w')
    for row in A:
        for j in row:
            file.write('%s\t' % str(j)),
        file.write('\n')
    file.close()

    file = open('MatFile.txt','r')
    B = [[int(num) for num in line.split()] for line in file]
    file.close()
    
    print(A)
    print(B)
    
    C = squareRootMat(A)
    print(C)
    
    file = open('MatFile.txt','a+')
    for row in C:
        for j in row:
            file.write('%s\t' % str(j)),
        file.write('\n')
    file.close()