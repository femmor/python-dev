# condition_true if condition else condition_false

age = int(input("What is your age? "))
can_vote = True if age >= 18 else False
print("You are {} years old. Can vote?".format(age), can_vote)

