hour =int(input("How many hours have you worked?\n"))
wage = float(input("How much you made an hour?\n"))
withhold=float(input("How much do you want to WITHHOLD from pay\n"))
pay = ((hour) * (wage) - float(withhold))

if pay < 1000 :
    print("I need a raise")
else:
    print("OK")