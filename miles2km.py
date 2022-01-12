# Ask the user to input the number of miles

# Convert miles to kilometers (kilometers = miles * 1.60934)

# Print this for example: 5 miles equals 8.0467 kilometers

# user input
num_of_miles = input("Enter number of miles: ")

# convert to integer
num_of_miles = int(num_of_miles)

# convert miles to kilometers
miles_km = num_of_miles * 1.60934

print("{} miles equals {} kilometers".format(num_of_miles, miles_km))
