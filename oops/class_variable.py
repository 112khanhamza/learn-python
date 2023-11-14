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


e1 = Employee('Hamza', 'Khan', 25000)
e2 = Employee('Talha', 'Khan', 30000)

# print(e1.__dict__)
# print(Employee.__dict__)

# print(e1.pay)
# e1.apply_raise()
# print(e1.pay)

e2.raise_amt = 1.04 # important
print(e1.raise_amt)
print(e2.raise_amt)
print(e1.pay)
e1.apply_raise()
print(e1.pay)

print(Employee.num_of_emps)
e1.num_of_emps = 5
print(e1.num_of_emps)