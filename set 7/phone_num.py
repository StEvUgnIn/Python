import re

pattern = r'([+|(00)]41)|07[6789][0-9]{7}'
regex = re.compile(pattern, re.VERBOSE)

print('Please enter a swiss (CH) mobile phone number')
number = str(input())
if regex.match(re.sub(r'\s+', '', number)):
    print('this number', number, 'is valid.')
else:
    print('sorry, you did not choose a phone number or a mobile phone either.')
    print('please check your input.')