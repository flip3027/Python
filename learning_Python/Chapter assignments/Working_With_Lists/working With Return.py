def adding(value):
    print(value + 2) # So i can see it on screen
    return value + 2 # This makes the new value for the number

print('Give me a number please') #menu screen
n = int(input()) #inpur

while n != 50: # n = 8 before loop
    n = adding(n) # n , is changing everytime because new value is being
                    # put in adding (n) slot then checking loop to see
                    # if it is equal