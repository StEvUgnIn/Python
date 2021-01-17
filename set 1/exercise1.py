#!/usr/bin/env python
# Python 3.6 added new string interpolation method called literal string interpolation and introduced a new literal prefix f. This new way of formatting strings is powerful and easy to use. It provides access to embedded Python expressions inside string constants.
import sys

sys.stdin.flush()
name   = str(input('What is your name? '))
sys.stdin.flush()
age    = int(input('How old are you? '))
sys.stdin.flush()
height = int(input('How tall are you? [cm] '))
sys.stdin.flush()
weight = int(input('How much do you weigh? [kg] '))

print(f'Hello {name}, so, you\'re {age} years old, {height} cm tall and {weight} kg heavy.')