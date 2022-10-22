hour =int(input("How many hours have you worked?"))
wage = float(input("How much you made an hour?"))
withhold=float(input("How much do you want to WITHHOLD from pay"))
pay = ((hour) * (wage) - float(withhold))

if pay < 1000 :
    print("I need a raise")
else:
    print("OK")