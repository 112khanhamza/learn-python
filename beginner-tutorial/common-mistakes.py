nums = [11, 30, 44, 54]

for num in nums:
	square = num ** 2
	print(square)


# Below Code executed wiered behaviour - 
# Python default arguments are evaluated once at the time of creating the function
# def add_employees(emp, emp_list=[]):
# 	emp_list.append(emp)
# 	print(emp_list)

# emps = ['John', 'Jane']

# add_employees('Hamza', emps)

# add_employees('Hamza')
# add_employees('Talha')
# add_employees('Maaz')


# In order to get an empty list each time
def add_employees(emp, emp_list=None):
	if emp_list is None:
		emp_list = []
	emp_list.append(emp)
	print(emp_list)

emps = ['John', 'Jane']

add_employees('Hamza', emps)

add_employees('Hamza')
add_employees('Talha')
add_employees('Maaz')

"""Below code will display weired behaviour
because even after waiting for a second the time is not changing.
Reason - in python default arguments are evaluated only once.
"""
# import time
# from datetime import datetime

# def display_time(time=datetime.now()):
# 	print(time.strftime('%B %d, %Y %H:%M:%S'))

# display_time()
# time.sleep(1)
# display_time()
# time.sleep(1)
# display_time()
# time.sleep(1)

# Fix
import time
from datetime import datetime

def display_time(time=None):
	if time is None:
		time = datetime.now()
	print(time.strftime('%B %d, %Y %H:%M:%S'))

# display_time()
# time.sleep(1)
# display_time()
# time.sleep(1)
# display_time()
# time.sleep(1)

# ITERATORS CAN BE EXHAUSTIVE
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

identities = zip(names, heroes)
print(list(identities))

# This for loop will not work
for identity in identities:
	print('{} is actually {}!'.format(identity[0], identity[1]))


# FIX
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

identities = list(zip(names, heroes))
print(identities)

# Now this for loop will work
for identity in identities:
	print('{} is actually {}!'.format(identity[0], identity[1]))


