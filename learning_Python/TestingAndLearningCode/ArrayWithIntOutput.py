place = ("","London","Paris","Lisbon","Sydney","Baku","Pretoria","Buenos Aires","Toyoko")

try:
    num = int(input("Enter a whole number between 1 and 7"))
    if num in range(1, 7):
        print(place[num])
    else:
        print("The number can only be between 1 and 7 ")
except ValueError:
    print('That was not a number between 1 and 7')
