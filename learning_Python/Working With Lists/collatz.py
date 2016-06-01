#Function
def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        number % 2 == 1
        print(3 * number + 1)
        return 3 * number + 1

#Menu
print('Enter a number:')
ct = 0

while ct != 1:
    try:
        number = int(input())
        ct += 1
    except ValueError:
        print('!!Please Enter an Integer!!:')


#Loop
while number != 1:
    number = collatz(number)

