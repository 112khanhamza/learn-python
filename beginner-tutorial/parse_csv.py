import csv

# with open('names.csv', 'r') as csv_file:
# 	csv_reader = csv.reader(csv_file)

# 	with open('new_names.csv', 'w') as new_file:
# 		csv_writer = csv.writer(new_file, delimiter='-')

# 		for line in csv_reader:
# 			csv_writer.writerow(line)

# with open("new_names.csv") as csv_file:
# 	csv_reader = csv.reader(csv_file, delimiter='-')
# 	for line in csv_reader:
# 		print(line)


# with open('names.csv', 'r') as csv_file:
# 	csv_reader = csv.DictReader(csv_file)

# 	for line in csv_reader:
# 		print(line['email'])

# with open('names.csv', 'r') as csv_file:
# 	csv_reader = csv.DictReader(csv_file)

# 	with open('new_names.csv', 'w') as new_file:
# 		fieldnames = ['first_name', 'last_name', 'email']
# 		csv_writer= csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
# 		csv_writer.writeheader()

# 		for line in csv_reader:
# 			csv_writer.writerow(line)


# html_output = ''
# names = []

# with open('patreon.csv', 'r') as data_file:
# 	csv_data = csv.reader(data_file)

# 	next(csv_data)
# 	next(csv_data)

# 	for line in csv_data:
# 		if line[0] == 'No Reward':
# 			break
# 		names.append(f"{line[0]} {line[1]}") # only works in python 3.6

# html_output += f'<p>There are currently {len(names)} public contributors. Thank you</p>'

# html_output += '\n<ul>'

# for name in names:
# 	html_output += f'\n\t<li>{name}</li>'

# html_output += '\n</ul>'

# print(html_output)


# Using Dictonary Reader - Preffred
html_output = ''
names = []

with open('patreon.csv', 'r') as data_file:
	csv_data = csv.DictReader(data_file)

	# we dont want first line of bad data
	next(csv_data)

	for line in csv_data:
		if line['FirstName'] == 'No Reward':
			break
		names.append(f"{line['FirstName']} {line['LastName']}") # only works in python 3.6

html_output += f'<p>There are currently {len(names)} public contributors. Thank you</p>'

html_output += '\n<ul>'

for name in names:
	html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)

