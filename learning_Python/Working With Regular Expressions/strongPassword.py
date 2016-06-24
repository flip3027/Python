#! python3

import re, pyperclip

#Todo: make a password regex
passwordRegex = re.compile(r'''
(?=.*[0-9])       # match zero or more Digits
(?=.*[a-z])       # match zero or more lowercase letters
(?=.*[A-Z])       # match zero or more Uppercase
(?=.*()).{8,}     # make sure password length is 8 characters long
''', re.VERBOSE)

#Todo: make a screen prompt telling the user what to do
print('''Enter a password: ''')
print('\t (must have at least: 1 uppercase, 1 lowercase, 1 number and 8 characters long)')
#Todo; put user's into a variable
text = str(input())
#Todo: Test user's input against the regex
#Todo: if strong tell user then copy to clipboard else tell user to run again
if passwordRegex.search(text) is not None:
    print('Password IS strong')
    print(text, ': has been copied to clipboard')
    pyperclip.copy(text)
else:
    print('Password NOT strong enough')
    print('Please run again and make strong password, Goodbye')


