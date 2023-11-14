try:
	f = open('text.txt', 'r') # this will not throw an error

	# manually raise an exception
	if f.name == 'text.txt':
		raise Exception
	# var = bad_var # this will throw error
except FileNotFoundError:
	print('Sorry. This file does not exists!')
except Exception as e:
	print('Sorry something went wrong:', e)
# if the try block does not throw an exception
else:
	print(f.read())
	f.close()
# runs if we throw exception or not
finally:
	print('Executing Finally...')
