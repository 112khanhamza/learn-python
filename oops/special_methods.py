import datetime

class Employee:

	raise_amt = 1.05 # this is a class variable (will remain the same for all new instances but can be modified)
	num_of_emps = 0 
	
	# constructor
	def __init__(self, first, last, pay):
		self.first = first # this is an instance variable (can be unique for each instance)
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	# this is a class method
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	# class method as alternative constructor
	@classmethod
	def from_string(cls, emp_str):
		first, last, age = emp_str.split('-')
		return cls(first, last, age)

	# static method (if you dont access the instance or the class anywhere in the function)
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

	# special methods
	# methods surrounded by double underscores are called as special/magic/dunder methods
	
	# something which can be used to recreate this object
	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

	# toString method
	def __str__(self):
		return '{} - {} - {}'.format(self.first, self.last, self.pay)

	# when we try to add two objects
	def __add__(self, other):
		return self.pay + other.pay

	# when we try to invoke length on an object
	def __len__(self):
		return len(self.fullname())


e1 = Employee('Hamza', 'Khan', 25000)
e2 = Employee('Talha', 'Khan', 30000)


print(e1)
print(e1+e2)
print(len(e1))