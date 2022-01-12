# Enter Calculation
num_1, operator, num_2 = input("Enter Calculation: ").split()
num_1 = int(num_1)
num_2 = int(num_2)

if operator == "+":
    print("{} + {} = {}".format(num_1, num_2, num_1 + num_2))
elif operator == "-":
    print("{} - {} = {}".format(num_1, num_2, num_1 - num_2))
elif operator == "*":
    print("{} * {} = {}".format(num_1, num_2, num_1 * num_2))
elif operator == "/":
    print("{} / {} = {}".format(num_1, num_2, num_1 / num_2))
elif operator == "%":
    print("{} % {} = {}".format(num_1, num_2, num_1 % num_2))
else:
    print("Please add an operation")


