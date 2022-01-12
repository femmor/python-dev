import sys

'''
Variables in python
'''

# my_name = "Reign"
# my_age = 35

# print("Hello!", my_name)

# print(sys.maxsize)

# print("2 + 2", "=", int(2) + int(2))

# Input
# name = input("What is your name? : ")
# print("Hello", name)

num_1, num_2 = input("Enter 2 numbers : ").split()
num_1 = int(num_1)
num_2 = int(num_2)

sum_1 = num_1 + num_2
diff = num_1 - num_2
product = num_1 * num_2
quotient = num_1 / num_2
remainder = num_1 % num_2

# Result
print("{} + {} = {}".format(num_1, num_2, sum_1))
print("{} - {} = {}".format(num_1, num_2, diff))
print("{} * {} = {}".format(num_1, num_2, product))
print("{} / {} = {}".format(num_1, num_2, quotient))
print("{} % {} = {}".format(num_1, num_2, remainder))


# print("Sum of the 2 numbers is :", sum_1)
# print("Difference of the 2 numbers is :", diff)
# print("Product of the 2 numbers is :", product)
# print("Dividing the 2 numbers is :", quotient)
# print("The remainder of the 2 numbers is :", remainder)

