#!/usr/bin/env python
import random, sys

"""
How should you avoid choosing the same number again? How can you repeat it to play multiple games?
- with a gaussian random but you need to provide some mean and some variance 
"""
def main():
    numbers = [random.randint(1,50) for i in range(0,5)]
    star_numbers = [random.randint(1, 12) for i in range(0,2)]

    print(numbers)
    print(star_numbers)

if __name__ == "__main__":
    main()