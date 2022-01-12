# Conditional Operators

drink = input("Please choose a drink (Coke or Pepsi)? : ")

if drink == "Coke":
    print("Here is your {}".format(drink))
elif drink == "Pepsi":
    print("Here is your {}".format(drink))
else:
    print("Here is your Water")