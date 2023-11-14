student = {'name': 'Hamza', 'age': 25, 'courses': ['math', 'compsci']}

print(student)

# access specific field
print(student['name'])
print(student['courses'])

# key can be any immutable data-type
student = {1: 'Hamza', 'age': 25, 'courses': ['math', 'compsci']}
print(student[1])

student = {'name': 'Hamza', 'age': 25, 'courses': ['math', 'compsci']}

# key that does not exists
# print(student['phone']) # throws error
print(student.get('age'))
print(student.get('phone')) # returns None

# get default value if key does not exists
print(student.get('phone', 0))

# add new entry
student['phone'] = '555-5555'
print(student.get('phone', 'Not Found'))
print(student)

student['name'] = 'Maaz'
print(student)

# using update takes in dictonary
student.update({'name': 'Talha', 'age': 26})
print(student)

# delete a key
del student['phone']
print(student)

# using pop to delete
age = student.pop('age')
print(age)
print(student)

# looping through dict
student = {'name': 'Hamza', 'age': 25, 'courses': ['math', 'compsci']}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
	print(key, value)






