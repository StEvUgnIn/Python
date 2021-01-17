#!/usr/bin/env python

num = abs(int(input('Enter any number [N+] ')))

print('Diviseurs communs: ', end='')
for i in range(1, num+1):
    if num % i == 0:
        print(i, ' ', end='')
print()