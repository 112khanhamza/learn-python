li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li) # returns a new sorted list
# li.sort() # will sort the original list

print('sorted variable: \t',s_li)
print('original variable: \t',li)

s_desc_li = sorted(li, reverse=True)
print('sorted desc list: \t', s_desc_li)

tup = (9,1,8,2,7,3,6,4,5)
# tup.sort() # error- no such method
s_tup = sorted(tup)
print('sorted tuple: \t', s_tup)

di = {'name': 'hamza', 'job': 'programming', 'age': None, 'os': 'mac'}
s_di = sorted(di)
print('sorted dictionary: \t', s_di) # will sort the keys

li = [-6,-5,-4,1,2,3]
s_li = sorted(li)
print(s_li)

# sort based on absolute value
s_li = sorted(li, key=abs)
print('sorted list abs value: \t', s_li)

class Employee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return '({},{},${})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Hamza', 25, 90000)
e3 = Employee('Talha', 22, 19000)
e4 = Employee('Maaz', 21, 40000)

employees = [e1, e2, e3, e4]

def e_sort(emp):
	return emp.name

# using function
s_employees = sorted(employees, key=e_sort, reverse=True)

# using lambda
s_employees = sorted(employees, key=lambda e: e.salary, reverse=True)

# using attrgetter
s_employees = sorted(employees, key=attrgetter('age'), reverse=True)
print(s_employees)
