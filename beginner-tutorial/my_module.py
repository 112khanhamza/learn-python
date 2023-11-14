print('Importing my_module.py...')

def find_index(search_string, target):
	for i, value in enumerate(search_string):
		if value == target:
			return i
	return -1