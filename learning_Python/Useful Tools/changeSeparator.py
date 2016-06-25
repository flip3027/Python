#! python3

import pyperclip

print('Please enter what you would like as a separator')
separator = str(input())
def changeSeparator(separator):
    text = pyperclip.paste()
    '''
    TODO: put sentences into individual strings with the spilt module
    brake at ' ' then
    pass the strings into in a for loop that adds "separator" then the sentence then
    use join module at 'separator' because pyperclip.copy only take 1 string all together.
    '''
    lines = text.split(' ')

    for i in range(len(lines)):
        lines[i] = '' + lines[i]
    text = separator.join(lines)
    pyperclip.copy(text)
    print('The text has copy to the clipboard with ' + separator + "'s")

changeSeparator(separator)
