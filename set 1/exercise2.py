#!/usr/bin/env python
import cmath, math, sys

sys.stdin.flush()
number = float(input('Enter a number: '))
print(f'{str(abs(number))}')

sys.stdin.flush()
a = float(input('Enter a number: '))
print(f'{math.log(a, 10)}')

sys.stdin.flush()
pos = int(input('Enter a positive integer: '))
print(f'Factorial: {math.factorial(pos)}')

sys.stdin.flush()
neg_real = float(input('Enter a negative number: '))
print(f'Floor: {math.floor(neg_real)}')
print(f'Ceil:  {math.ceil(neg_real)}')

sys.stdin.read(1)
print(f'Exponential of 7: {math.exp(7)}')

sys.stdin.read(1)
print(f'pi: {math.pi}')
print(f'e:  {math.e}')

sys.stdin.read(1)
print(f'cos(pi):   {math.cos(math.pi)}')
print(f'sin(pi/6:  {math.sin(math.pi/6)}')
print(f'arctan(1): {math.atan(1)}')

sys.stdin.flush()
a = float(input('Enter two real numbers: '))
b = float(input())
z = complex(a, b)
print(f'Absolute value of a complex number: {z.__abs__()}')