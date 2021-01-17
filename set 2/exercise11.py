#!/usr/bin/env python
number = abs(int(input('Enter a positive value ')))
facto = 1
for i in range(0, number):
    facto *= i + 1

print(number, '! = ', facto, sep='')