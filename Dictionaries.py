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
    "completed_lesson_name": ["operators", "data types", "variables"]


}

print(devops_students)
# print(type(devops_students))
# display data by fetching the key name
# print(devops_students["name"])

# prints the keys
# print(devops_students.keys())

# how can we fetch the value called "data types"
print(devops_students["completed_lesson_name"][1])

