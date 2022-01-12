# Logical Operators

# and - if both are true returns true
# or - if either is true returns true
# not - converts true to false and vice-versa

# Determine whether a birthday is important or not
# 1 - 18 -> Important
# 21, 50, > 65 -> Important
# All others -> Not Important

age = int(input("Enter age: "))

if (age >= 1) and (age <= 18):
    print("Birthday is important")
elif (age == 21) or (age == 50):
    print("Birthday is important")
elif not age < 65:
    print("Birthday is important")
else:
    print("Birthday is not important")