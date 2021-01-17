#!/usr/bin/env python

number = int(input('Enter a positive number '))
res = ''

while number != 0:
    res = str(number % 2) + res
    number //= 2

print(res)