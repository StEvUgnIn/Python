#!/usr/bin/env python

num1 = abs(int(input('Enter any number [N+] ')))
num2 = abs(int(input('Enter any number [N+] ')))

print('Diviseurs communs: ', end='')
for i in range(1, num1+1 if num1 > num2 else num2+1):
    if num1 % i == 0 and num2 % i == 0:
        print(i, ' ', end='')
print()