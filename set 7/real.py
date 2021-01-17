import re

pattern = r'^[+-]?[0-9]+[.]?[0-9]*[eE]?[+]?[0-9]*$'
regex = re.compile(pattern)

print('Please enter any real number')
print()
if regex.match(input()):
    print('this is a real number')
else:
    print('this is not a real number')