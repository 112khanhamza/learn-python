'''
LEGB
Local, Enclosing, Global, Built-in
'''

import builtins
# print(dir(builtins))

######BUILTIN SCOPE#########
def min():
	pass

# m = min([5,1,4,2,3]) # this will throw an error
# print(m)

######GLOBAL SCOPE#########
x = 'global x'

def test(z):
	# global x

	######LOCAL SCOPE#########
	x = 'local x'
	# print(y)
	print(x)
	print(z)

test('local z')
# print(y) # this will give an error
print(x)
# print(z) # this will give an error

#######ENCLOSING SCOPE#########
def outer():
	x = 'outer x'

	def inner():
		# nonlocal x # to work with x which is in the outer function
		# x = 'inner x'
		print(x)

	inner()
	print(x)

outer()
print(x)