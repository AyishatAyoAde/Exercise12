# What is wrong with this?
# The += argument is a wrong way of adding to a list as it treats the string as a sequence of characters rather than as an item

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke'
print(cheese)

# How should 'Oke' be added to the end of the cheese list?
# Append is a method that is used to add an item to a list

cheese.append('Oke')
print(cheese)

# How would you add two new cheeses to the list with a single command?
# The extend method is used to add multiple items to the end of a list
cheese.extend(['Brie', 'Camembert'])
print(cheese)