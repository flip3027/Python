#! python3

import pyperclip, re

#Todo: make a phone regex
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?      # area code
(\s|-|\.)?              # separator
(\d{3})                   # first 3 digits
(\s|-|\.)               # separator
(\d{4}))                  #last 4 digits
''', re.VERBOSE)
# Todo: Make a email regex and verbose to end of string
emailRegex = re.compile(r'''(
[a-zA-z0-9._%+-]+   #username
@                   # @ symbol
[a-zA-z0-9.-]+      # domain name
(\.[a-zA-Z]{2,4})   # dot-something
)''', re.VERBOSE)

#Todo: get info from pyperclip module
text = str(pyperclip.paste())

#Todo: go thru text and FINDALL MATCHES
matches = []

for groups in phoneRegex.findall(text):
    phonenum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phonenum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Todo: copy matches to pyperclip
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')
