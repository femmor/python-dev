# 1. Have the User enter their investment amount and expected interest
# 2. Each year their investment will increase by (investment + investment * interest)
#  3. Print out earnings after a 10 year period

# Solution
money = float(input("Enter investment amount: "))
interest_rate = float(input("Enter interest rate: ")) * 0.01

for i in range(11):
    money = money + money * interest_rate
    if (i == 10):
        print("Your earning is ${:.2f} after {} years of investment ".format(money, i))

