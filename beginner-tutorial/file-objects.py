# f = open('text.txt', 'r') # open file for reading
# f = open('text.txt', 'w') # open file for writing
f = open('text.txt', 'a') # open file for appending
f = open('text.txt', 'r+') # open file for reading and writing

# f = open('text.txt', 'r') # open file for reading

# print(f.name)
# f.close() # you will have to explicitly close the file
# print(f.mode)

# auto-closable (context manager)
# with open('text.txt', 'r') as f:
# 	f_contents = f.read()
# 	print(f_contents)

# with open('text.txt', 'r') as f:
# 	f_contents = f.readlines()
# 	print(f_contents)


# with open('text.txt', 'r') as f:
# 	for line in f:
# 		print(line, end='')

with open('text.txt', 'r') as f:
	size_to_read = 10 # reads 10 characters
	f_contents = f.read(size_to_read)
	while len(f_contents) > 0:
		print(f_contents, end='*')
		f_contents = f.read(size_to_read)


with open('text.txt', 'r') as rf:
	with open('out.txt', 'w') as wf:
		for line in rf:
			wf.write(line)

# reading and writing in bytes
with open('text.txt', 'rb') as rf:
	with open('out.txt', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)


