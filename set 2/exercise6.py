#!/usr/bin/env python
i = 0
num = [None]
while num[i] != 0:
    num.append(abs(int(input('Enter any number [N+] '))))
    i += 1
num.remove(None) # None
num.pop() # 0
num.sort()
print('Diviseurs communs: ', end='')
for i in range(1, num[0]+1):
    isCommonDivider = True
    for j in range(0, len(num)):
        if num[j] % i != 0:
            isCommonDivider = False
            break
    if isCommonDivider == True:
        print(i, ' ', end='')
print()