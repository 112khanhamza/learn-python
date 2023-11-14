class Employee:

	# constructor
	def __init__(self, first, last, pay):
		self.first = first # this is an instance variable (can be unique for each instance)
		self.last = last
		self.pay = pay

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print('Delete Name!')
		self.first = None
		self.last = None

e1 = Employee('Hamza', 'Khan', 25000)

e1.first = 'Jim'
e1.fullname = 'Hamza Ansari'

print(e1.first)
print(e1.email)
print(e1.fullname)

del e1.fullname
print(e1.fullname)