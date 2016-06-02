#class and methods

class A:
    def add(self, x , y):
        return x + y

class B(A):
    def sub(self, x, y):
        return x - y

class C(B):
    def multiple(self, x, y):
        return x * y

class D(C):
    def divide(self, x, y):
        return  x / y

#varibles
calculator = D()
choice = 0
check = 0
num1 = 0
num2 = 0

#Menu
print('Select Operation')
print('1.Add')
print('2.Subtract')
print('3.Multiple')
print('4.Divide')

#Choice loop
while choice < 1 or choice > 4:
    try:
        choice = int(input('Enter a choice 1/2/3/4:'))
    except ValueError:
        print('Choose 1/2/3/4:')
#Program
while True:
    try:
        num1 = int(input('Enter the first number'))
        num2 = int(input('Enter the second number'))
        break
    except ValueError:
        print("HEY! '{}' is not a Interger!")

# Output Answers
try:
    if choice == 1:
        print(str(num1) , '+' ,str(num2) , '=' , calculator.add(num1, num2))
    elif choice == 2:
        print(str(num1), '-', str(num2), '=', calculator.sub(num1, num2))
    elif choice == 3:
        print(str(num1), '*', str(num2), '=', calculator.multiple(num1, num2))
    elif choice == 4:
        print(str(num1), '/', str(num2), '=', calculator.divide(num1, num2))
except ZeroDivisionError:
    print(str(num1), '/', str(num2), '= 0' )

