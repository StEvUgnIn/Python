#!/usr/bin/env python

def main():
    print(fib(find_index(5)))

def fib(n):
    a,b = 1,1
    for _ in range(n-1):
        a,b = b,a+b
    return a

def find_index(i):
    for n in range(i+1):
        if fib(n) == i:
            return n
    return -1

if __name__ == "__main__":
    main()