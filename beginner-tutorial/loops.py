nums = [1, 2, 3, 4, 5]

for num in nums:
	if num == 3:
		print('Found 3')
		break
	print(num)

print('=========Loop===========')
for num in nums:
	if num == 3:
		print('Found 3')
		continue
	print(num)

print('=========Nested Loop===========')
for num in nums:
	for letter in 'abc':
		print(num, letter)

print('==========Range==========')
for i in range(10):
	print(i)

print('==========Range start end==========')
for i in range(1, 11):
	print(i)

print('==========While loop==========')
x = 0
while x < 10:
	print(x)
	x += 1

