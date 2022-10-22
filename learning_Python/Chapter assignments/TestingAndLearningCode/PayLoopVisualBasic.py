wkCt = 0

while wkCt < 3 :
    name = input("Enter a name")
    hour = int(input("How many hours have you worked?"))
    wage = float(input("How much you made an hour?"))
    withhold = float(input("How much do you want to WITHHOLD from pay"))
    pay = ((hour) * (wage) - float(withhold))
    if pay < 1000:
        print(name, "needs a raise")
        wkCt= wkCt +1
    else:
        print(name,"is OK")
