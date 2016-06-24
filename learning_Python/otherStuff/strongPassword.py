#! python3

import re, pyperclip

passwordRegex = re.compile(r'''
(?=.*[0-9])       # match zero or more Digits
(?=.*[a-z])       # match zero or more lowercase letters
(?=.*[A-Z])       # match zero or more Uppercase
(?=.*()).{8,}     # make sure password length is 8 characters long
''', re.VERBOSE)

print('''Enter a password: ''')
print('\t (must have at least: 1 uppercase, 1 lowercase, 1 number and 8 characters long)')
text = str(input())

if passwordRegex.search(text) is not None:
    print('Password IS strong')
    print(text, ': has been copied to clipboard')
    pyperclip.copy(text)
else:
    print('Password NOT strong enough')
    print('Please run again and make strong password, Goodbye')


