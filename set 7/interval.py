import re

string='right interval with lower and upper limits'
real_pattern = r'[+-]?[0-9]+[.]?[0-9]*[eE]?[+]?[0-9]*'
pattern = r'[[]?[ \t]*({0}),[ \t]*({0})[ \t]*[]]?'.format(real_pattern)
regex = re.compile(pattern)

print('Please enter any', string)
print()
interval = input()
if regex.match(interval):
    lower, upper = (regex.search(interval).group(i) for i in range(1, 3))
    print('limits')
    print('lower:', lower)
    print('upper:', upper)
    print('this is a', string)
else:
    print('this is not a', string)