#!/usr/bin/env python
import doctest

def binomialCoeff(n, k):
    """https://rosettacode.org/wiki/Evaluate_binomial_coefficients#Python"""
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) // i
    return result

def pascal(n):
    for i in range(1, n+1):
        for j in range(i+1):
            print(binomialCoeff(i, j), end='\t')
        print()

if __name__ == "__main__":
    pascal(5)