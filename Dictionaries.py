# What is a dictionary
# Dictionary (use arrays) is another way of managing data but more dynamically
# key Value pairs to store and manage data
# syntax: {"name"(key): "james"(value)}
# What kind of data can we store/manage? any
# Why

devops_students = {
    "name": "Daniel",
    "Stream": "tech",
    "completed_lessons": 4,
    "Hobbies": ["football", "watches", "eating"]


}
#
# print(devops_students)
# # print(type(devops_students))
# # display data by fetching the key name
# # print(devops_students["name"])
#
# # prints the keys
# # print(devops_students.keys())
#
# # how can we fetch the value called "data types"
# print(devops_students["completed_lesson_name"][1])
#
# # how can i change the value of a specific key
# devops_students["completed_lessons"] = 3
#
# # everything in the dictionary
# print(devops_students.items())

# task: create a new dictionary to store user data
# user_info = {
#     "name": "Daniel",
#     "DOB": "8/12/1995",
#     "address": "99 north street",
#     "course": "mechanical engineering",
#     "grades": "second class",
#     "Hobbies": ["football", "watches", "eating"]
#
#
# }
#
# # create a list of hobbies, at least 3 items
# # all the details that you utilised in the last task, name, DOB, address, course, grades
# # remove, add, replace, display the type of items
# user_info[].pop() # remove last item
# user_info["age"] = 12 # add
# user_info[].replace["course"] = "tech" # replace
# user_info(type() # display data type
# # display in reverse
# print(user_info["hobbies"][::-1]))
# print(user_info)

# add to the list, hobbies
devops_students["Hobbies"].append("running")
print(devops_students)

# remove from the list, hobbies
devops_students["Hobbies"].remove("watches")





