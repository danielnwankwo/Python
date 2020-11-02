# # What is concatenation
# first_name = "James"
# middle_name = "Bond"
# last_name = "007"
# age = 18
#
# #James Bond 007
#
# print(first_name)
# print(middle_name)
# print(last_name)
#
#
# print(first_name + " " + middle_name + " " + last_name)
#
# # Casting is used to cast integers to strings or visa versa
# # str()
# print(first_name + " " + middle_name + " " + last_name + " " + str(age))
# .....

# name = input("PLease enter your name ")
# print("hello " + name)

# get user info
# DOB
# address - first line and house number + post code

# input("What is your name? ")
# input("What is your DOB? ")
# input("How old are you? ")

name = input("What is your name ? ")
DOB = input("What is your DOB in the format dd/mm/yyyy? ")
age = input("How old are you ? ")
House_number = input("please enter your house number")
First_line_address = input("whats is your first line of address ")
Post_code = input("please enter your post code ")

Print("Hello " + name)
Print("Your DOB seems to " + DOB)
Print("You are " + age)
print("your house number = " + int(House_number))
print(First_line_address)
Print(Post_code)

# Declaring strings with double and single quotes
# "" as well as ''
# single_quotes = 'single quotes\'wow\''
# print(single_quotes)
# double_quotes = "double quotes 'wow'"
# print(double_quotes)

# string slicing - why -
# indexing in python starts from 0

# this will print the whole word
 greetings = "Hello world!"
 print(greetings)
# prints just Hello - not including 5th character
greetings = "Hello world!"
print(greetings[0:5])

# length - how many characters
print(len(greetings))

# Python counts empty spaces as characters
white_spaces = " lots of spaces as the ends                      "
print(len(white_spaces))

#strip() deletes all the empty space at the end of a string
print(len(white_spaces.strip()))

# Count() - counts the number of times any word is available in a string

example_text = "lots of text with some text                        "
print(example_text.count("text"))

# replace with and put ','
print(example_text.replace("with", ","))

# capitalize the first letter of the sentence

print(example_text.capitalize())
# everything uppercase
print(example_text.upper())
# everything lowercase
print(example_text.lower())










