#! python3

import sys, pyperclip, shelve

myData = shelve.open(r'C:\playground\pythonScripts\mcb')
option = ['save', 'list', 'recall' , 'delete', 'clear']


if len(sys.argv) == 3 and sys.argv[1].lower() == option[0]:
    myData[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == option[1]:
        pyperclip.copy(str(list(myData.keys())))
    elif sys.argv[1].lower() == option[2]:
        for key, value in myData.items():
            print('\n' + key, ': ', value + '\n')
    elif sys.argv[1].lower() == option[4]:
        for key, value in myData.items():
            del myData[key]
        print('All cleared'.center(20))
    elif sys.argv[1] in myData:
        pyperclip.copy(myData[sys.argv[1]])
elif sys.argv[1].lower() == option[3]:
    del myData[sys.argv[2]]



myData.close()

