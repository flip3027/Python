#! python3

import pyperclip

text = pyperclip.paste()

'''
TODO: put sentences into individual strings with the spilt module
brake at '\n'' then
pass the strings into in a for loop that adds '*' then the sentence then
use join module at '\n' because pyperclip.copy only take 1 string all together.
'''
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '*  ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
print('The text has copy to the clipboard with BULLETS')




