def function(list):
    list.insert(-1,'and')
    for i in list:
        print(i, end=', ')
spam = ['apple', 'bananas', 'tofu', 'cats']
#print(spam)

function(spam)