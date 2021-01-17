#!/usr/bin/env python
import random, sys

def main():
    i = 1
    n = random.randint(1, 100)
    m = None
    while m == None or m != n:
        sys.stdin.flush()
        entry = input(f'[{i}] Entrer un nombre [1-100] ')
        i += 1
        if entry == '':
            print('abandon...', end='')
            sys.stdin.read(1)
            exit(0)
        try:
            m = int(entry)
        except:
            print('SVP entrez un nombre valide')
            continue
        if m < 1 or m > 100:
            print('Min: 1, Max: 100')
        print('Trop petit' if m < n else 'Trop grand' if m > n else 'OK')

if __name__ == "__main__":
    main()