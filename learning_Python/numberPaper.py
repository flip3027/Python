#! python3
import pyperclip,sys

if len(sys.argv) < 2:
    print('Usage: py numberPaper.py[#] - copy numbers 1-#')
    sys.exit()
number = sys.argv[1]
def assignNumber(num):
    numList = []
    for i in range(num + 1):
        numList = numList + [i]
    for j in numList:
        numList[j] = str(j) + '\n'
    text = '\n'.join(numList)
    pyperclip.copy(text)
    print('You have numbers copied 0-' + str(num))




assignNumber(number)
