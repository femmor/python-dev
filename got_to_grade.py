import random
# If age is 5 "Go to Kindergaten"

# Ages 6 through 17 goes to grades 1 through 12 - "Go to Grade 6"

# Age is greater than 17 "Go to College"


age = int(input("Enter age: "))
if age < 5:
    print("Too young for school")
elif age == 5:
    print("Go to Kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to Grade {}".format(grade))
else:
    print("Go to College")