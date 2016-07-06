#! python3

import os, sys, re
'''
os.chdir('D:\\test')
print(os.getcwd())

# os.makedirs('D:\\create\\in\\python')

print(os.path.abspath('..'))

print(os.path.isabs('..' + ' This is not the absolute path of this directory'))

print(os.path.isabs(os.path.abspath('..' + ' It is true because the value of the absolute path is passed in as the arument')))

print(os.path.relpath('c:\\windows', 'c:\\'))

print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))

print(os.path.dirname('d:\\test'))
print(os.path.basename('d:\\test'))

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(calcFilePath))

calcFilePath.split(os.path.sep)

os.path.getsize('C:\\Windows\\System32\\calc.exe')



totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
      totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(totalSize)

list1 = ['jen', 'barbara', 'ann']
list2 = ['paul', 'bob', 'alex']


print(os.listdir('D:\\test'))
'''

file = open('D:\\test\\test1.txt')
content = file.read()
file.close()
print(content)

helloRegex = re.compile(r'''(
(\A\w+
)''',re.VERBOSE)
