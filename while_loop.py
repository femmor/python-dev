import random

# While Loop
# rand_number = random.randrange(1, 50)
# i = 1
#
# while i != rand_number:
#     i += 1
# print("The random number is {}".format(i))

i = 1
while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue
    if i == 15:
        break
    print("Odd:", i)
    i += 1