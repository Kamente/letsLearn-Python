# _age = 23
# print(_age)

# print("Hello", "Dear")
# print('My favorite colors are', 'blue', 'green', 'red')

# print("Hello" ", " "Dear")

# data types
# int age = 25
# string name = "Justin"
# float balance = 23.45
# boolean pass = True
# set: myMarks = {34, 20, 56, 78}
# Dictionary (key-value pairs) myDict = {'name': "Justin", 'age': 24}
# student = {'id': 2345, 'name': 'Justin'}
# print(student)


# my_range = range(5)
# print(type(my_range))

# studentInfo = ["Justin", 54, "Age"]
# print(studentInfo)

# grade = 45.56
# print(type(grade))

name = 'Alice'
print(name, type(name))

# isinstance check whether the datatype is the one
score = 56.4
print(isinstance(score, float))

# string concat
str1 = "Justin"
str2 = "Kim"
print(str1 + " " + str2)


# multiline (3 quotes)
str3 = """
Justin
Mugambi
Kamente
"""
print(str3)


message = "It's a sunny day"
print(message)

message2 = "It\'s a sunny day"
print(message2)


# in: checks whether a text or character exists in the string, e.g:
string1 = "My name is Justin"
print("am" in string1)
print("sti" in string1)


# indexing
print(len(string1))
print(string1[-1])


# interpolation (insert var & expressions): using f
name = "Kamente"
marks = 56
print(f'my name is {name} and i got {marks} in Chemistry')

whatIGot = f'my name is {name} and i got {marks} in Chemistry'
print(whatIGot)
