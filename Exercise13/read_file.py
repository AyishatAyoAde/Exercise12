# Use the *open* and *read* methods to slurp the entire contents of the pelican.txt file
# slurping reads entire file in one gulp
from os.path import split

# output = open('pelican.txt')

# for line in open('pelican.txt', 'r'):
#     print(line[:-1])
#
# # Display the type of the returned data and print the contents of the returned data
# # Had to bring back the output variable but without the character as it was printing the content that way
# # What data type is the output? : textio
# print(type(output))

# Write code that will read the pelican.txt file into a list and then output the number of items within the list

# output_list = str(output).split()
# print(output_list)

# opening and reading using the slurping method and displaying the type of the returned data and printing the content of the returned data

output = open('pelican.txt', 'r').read()
print(f"Whole song:\n{output}")
print(type(output))

# turning pelican.txt into a list and outputting the number of items within the list

song_into_list = output.split("\n")
print(song_into_list)
print(len(song_into_list))

print('*' * 40)

# Using a loop to iterate over and print the contents of the file

output = open('pelican.txt', 'rt')
for line in output:
     print(line, end='')
output.close()
