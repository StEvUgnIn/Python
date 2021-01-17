#!/usr/bin/env python
import time
import doctest

numCalls = counter = 0

def main():
    """entry point"""
    print('This program evalues execution time for recursive and memoization paradigms of fibonacci suite')
    start_time = time.time()
    print(fibR(30))
    elapsed_time = time.time() - start_time
    print('Recursive: %f' % elapsed_time)
    start_time = time.time()
    print(fibDict(30, dict()))
    elapsed_time = time.time() - start_time
    print('Memoization: %f' % elapsed_time)

def fibR(n):
    """Fibonacci algorithm based on recursivity"""
    global numCalls
    numCalls += 1
    if n==1 or n==2: 
        return 1
    return fibR(n-1)+fibR(n-2)

def fibDict(n, d):
    """Fibonacci algorithm based on memoization"""
    global counter
    counter+=1
    if n in d: 
        return d[n]
    if n==1 or n==2: 
        return 1
    else: 
        d[n] = fibDict(n-1, d)+ fibDict(n-2, d)
    return d[n]

if __name__ == "__main__":
    main()