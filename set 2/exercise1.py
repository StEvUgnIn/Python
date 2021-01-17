#!/usr/bin/env python
import sys

def main():
    num1 = 0
    num2 = 0
        
    if len(sys.argv) > 2:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    else:
        num1 = enter_number()
        num2 = enter_number()
    print('Greatest common divider between %i and %i: %i' % (num1, num2, Gcd(num1, num2)))

i = 0

def enter_number():
    global i
    i+=1
    return int(input('Enter an integer number [%d]: ' % i))

def Gcd(val1, val2):
    if abs(val1) > abs(val2): 
        val1, val2 = val2, val1
    gcd = abs(val1)
    if val2 % gcd != 0:
        while gcd > 0 and (val1 % gcd != 0 or val2 % gcd) != 0: gcd -= 1
    return gcd

if __name__ == "__main__":
    main()