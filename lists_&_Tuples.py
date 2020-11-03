# #Collection in Python
# # Lists?
# # Lists are mutable -
# # we can remove, add, change an item in the list
# # indexing starts with 0
# # "hello world"
# # syntax: ["Yogurt", "apple", "milk"]
#
# # Let's create a list
#
#
# print (type(shopping_list))
#
# # Look at indexing in list items
#
# print(shopping_list[1]) # just print milk
# print(shopping_list[2]) # just print bread
# print(shopping_list[-1]) # also prints just bread
#
# # Managing lists
# # add an item to this list
#
# shopping_list.append("eggs")
# # append method adds an item on to the end of the list
# print(shopping_list)
#
# # How can we remove an item from the list
# shopping_list.remove("apple")
# print (shopping_list)
#
# # how we can remove the last item from our list we appended earlier
# shopping_list.pop()
# print(shopping_list)
#
# # how can i replace an item in the list
# shopping_list[1] = "fruits" # puts fruits into that position replacing anything there already
# print(shopping_list)
#
# # how can we have mixed data types in the list
# mixed_shopping_list = [1, 2, 3, "apple", "milk", "bread"]
# print(mixed_shopping_list)
#
# # Task: create a mixed data type list of 7 items
# mixed_shopping_list = [1, 2, 3, "apple", "milk", "bread", "sausage"]
# print(mixed_shopping_list)
# display the type of data
# print((mixed_shopping_list)type())
# # add, delete, replace, pop,
# mixed_shopping_list.pop()
# mixed_shopping_list.append("cake")
# mixed_shopping_list.remove("sausage")
# mixed_shopping_list[2] = 4
# # use indexing to print the list in reverse order
# print(mixed_shopping_list[::-1])

# Tuples are immutable - cant be changed
# Use case NI number, DOB, place of birth etc
# syntax: we use () to declare a Tuple
short_list = ("paracetamol", "eggs", "supermalt", )
print(short_list)
# cannot do this as tuples do not allow us to change anything
short_list[1] = "fruits"
print(short_list)

