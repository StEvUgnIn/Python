#!/usr/bin/env python
import random, sys
from math import fsum

# modified from https://rosettacode.org/wiki/Random_numbers#Python
def quick_check(numbers):
    count = len(numbers)
    mean = fsum(numbers) / count
    variance = (fsum((i - mean)**2 for i in numbers) / count)
    return mean, variance

def getchar(): 
    sys.stdin.read(1)

def main():
    a=random.random(); print(a)
    getchar()

    b=random.randrange(-3.0, 5.0); print(b)
    getchar()

    c=random.randint(1, 100); print(c)
    getchar()

    mean, variance = quick_check([a, b, c])
    #print(mean)
    #print(variance)

    print(random.gauss(mean, variance))
    getchar()

if __name__ == "__main__":
    main()