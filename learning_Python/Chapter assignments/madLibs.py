#! python3
#madlibs.py

import re, shelve


keywordRegex = re.compile(r'''(
adjective|
verb|
noun
)''', re.IGNORECASE|re.VERBOSE)

file = open('madlibTest.txt')
file2 = open('test.txt', 'w')
content = file.read()
file.close()


for word in keywordRegex.findall(content):
    print(word)
file2.close()





file3 = open('test.txt')
content2 = file3.read()
file3.close()
print(content2)



