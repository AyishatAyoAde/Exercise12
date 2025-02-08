# Write a line of code to create a file handle to open and append to a file called pelican.txt

# output = open('pelican.txt', 'a')
# How do we stop the sting printing multiple times due to running it?
# The 'a' character causes it to print multiple times on each run that's why we changed it to a 'w'

output = open('pelican.txt', 'w')

# Append the following line to the file using the *write* method of the file handle:
# "A wonderful bird is the pelican"

output.write("A wonderful bird is the pelican\n")

# Append the following second line using the *write* method:
# "His bills holds more than his belican"

output.write("His bills holds more than his belican\n")

# Create a list that contains the following lines:
# lines = ["He can take in his beak,/n", "Enough food for a week,\n","But I'm damned if I see how the helican.\n"]
# Append the list to the following using the *writelines* method.
# Why are the "\n" required?: to make a new line

lines = ["He can take in his beak,\n", "Enough food for a week,\n","But I'm damned if I see how the helican.\n"]
output.writelines(lines)

# the writelines method is used to add a list to a file