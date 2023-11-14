# Comparisons:
# Equal:			==
# Not Equal: 		!=
# Greater Than: 	>
# Less Than: 		<
# Greater or Equal: >=
# Less or Equal: 	<=
# Object Identity: 	is

# and
# or
# not

if True:
	print('condition was true')

if False:
	print('condition was false')

language = 'java'

if language == 'python':
	print('language is python')
elif language == 'java':
	print('language is java')
elif language == 'javascript':
	print('language is javascript')
else:
	print('No match')


user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
	print('Admin page')
else:
	print('Bad Cred')

logged_in = False
if not logged_in:
	print('Please log in')
else:
	print('Welcome')


# Object identity
a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))
print(a is b) # two different objects in memory
print(a == b) # objects are simillar

# False Values:
	# False
	# None
	# Zero of any numeric type
	# Any empty sequence. For example, '', (), []
	# Any empty mapping. For example, {}.

condition = 0
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')









