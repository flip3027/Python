place = ("","London","Paris","Lisbon","Sydney","Baku","Pretoria","Buenos Aires","Tokyo")

try:
    num = int(input("Enter a whole number between 1 and 8:\n"))
    if num in range(1, 9):
        print(place[num])
    else:
        print("The number can only be between 1 and 7 ")
except ValueError:
    print('That was not a number between 1 and 7')
