#! python3

import pyperclip

print('Please enter a OLD separator')
oldSeparator = str(input())
print('Please enter a NEW separator')
newSeparator = str(input())

def changeSeparator():
    text = pyperclip.paste()
    '''
    TODO: put sentences into individual strings with the spilt module
    brake at ' ' then
    pass the strings into in a for loop that adds "separator" then the sentence then
    use join module at 'separator' because pyperclip.copy only take 1 string all together.
    '''
    lines = text.split(oldSeparator)

    for i in range(len(lines)):
        lines[i] = '' + lines[i]
    text = newSeparator.join(lines)
    pyperclip.copy(text)
    print('The text has copy to the clipboard with ' + newSeparator + "'s")

changeSeparator()
