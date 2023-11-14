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
		self.pay = self.pay * self.raise_amt

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


e1 = Employee('Hamza', 'Khan', 25000)
e2 = Employee('Talha', 'Khan', 30000)

Employee.set_raise_amt(1.03)
print(Employee.raise_amt)
print(e1.raise_amt)
print(e2.raise_amt)

emp_str_1 = 'Maaz-Khan-70000'
e3 = Employee.from_string(emp_str_1)
print(e3.first)

my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))