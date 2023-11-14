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

class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	raise_amt = 1.07

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, employee):
		if employee not in self.employees:
			self.employees.append(employee)

	def remove_emp(self, employee):
		if employee in self.employees:
			self.employees.remove(employee)

	def print_emps(self):
		for emp in self.employees:
			print('---->', emp.fullname())

dev_1 = Developer('Hamza', 'Khan', 50000, 'python')
dev_2 = Developer('Talha', 'Khan', 30000, 'java')

# print(help(Developer))

# print(dev_1.email)
# print(dev_2.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_1.prog_lang)

mgr_1 = Manager('Maaz', 'Khan', 90000, [dev_1])

# print(mgr_1.email)
# mgr_1.print_emps()
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))