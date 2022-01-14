# 1. Have the User enter their investment amount and expected interest
# 2. Each year their investment will increase by (investment + investment * interest)
#  3. Print out earnings after a 10 year period

# Solution
money = float(input("How much to invest: "))
interest_rate = float(input("Your interest rate: ")) * .01

for i in range(10):
    money = money + money * interest_rate
print("Investment after 10 years = ${:.2f}".format(money))
