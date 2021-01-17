#!/usr/bin/env python
number = int(input('Enter a positive number '))
base = 0
while base < 2 or base > 8:
# possible to create a code table for digits between 16 and 36.
# 10:15 are to be defined by A:F    
    base = int(input('Enter the conversion base '))  
res = ''
while number != 0:
    res = str(number % base) + res
    number //= base
print(res)