#!/usr/bin/env python
import numpy, sys

def main():
    fract1 = fraction(*entrer_fraction())
    fract2 = fraction(*entrer_fraction())
    print(fract1)
    print(fract2)
    somme  = fract1 + fract2
    print (somme)
    

def entrer_fraction():
    sys.stdin.flush()
    numerateur = int(input('Entrer un numerateur [N] '))
    denominateur = 0
    while denominateur == 0:
        denominateur = int(input('Entrer un denominateur [N*] '))
    return numerateur, denominateur
    
class fraction:
    def __init__(self, numerateur, denominateur):
        self.numerateur = int(numerateur)
        self.denominateur = int(denominateur) if denominateur != 0 else None

    def __add__(self, other):
        sum = fraction (
            self.numerateur * other.denominateur + other.numerateur * self.denominateur, 
            self.denominateur * other.denominateur
        )
        gcd = Gcd(sum.numerateur, sum.denominateur)
        sum.denominateur = int(sum.denominateur / gcd)
        sum.numerateur = int(sum.numerateur / gcd)
        return sum

    def __radd__(self, other):
        self.__add__(other)

    def __str__(self):
        return f'{__name__}: {self.numerateur} / {self.denominateur}'
    
def Gcd(val1, val2):
    if abs(val1) > abs(val2): 
        val1, val2 = val2, val1
    gcd = abs(val1)
    if val2 % gcd != 0:
        while gcd > 0 and (val1 % gcd != 0 or val2 % gcd) != 0: gcd -= 1
    return gcd

if __name__ == "__main__":
    main()