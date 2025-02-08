#Write a python script called lotto.py
#That will generate and display 6 unique random lottery numbers between 1-50.
#Which data structure is best suited to store the numbers?
#Use the Python help() function to find out which function to use from the python standard library called random

import random
random_numbers = [random.randint(1, 50) for i in range(6)]
print(random_numbers)

# imported the random module
# created a variable called random_numbers
# We used the randint method from the random module which is a method that identifies a random integer
# 1 - 50 is the min and max for our random numbers
# range is the number of integers printed