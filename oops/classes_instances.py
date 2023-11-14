# Python Object-Oriented Programming

class Employee:
	
	# constructor
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)


e1 = Employee('Hamza', 'Khan', 25000)
e2 = Employee('Talha', 'Khan', 30000)

print(e1.email)
print(e2.fullname())

print(Employee.fullname(e1))