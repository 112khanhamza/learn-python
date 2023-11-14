# lists, tuples and sets

courses = ['history', 'math', 'physics', 'compsci']
print(courses)
print(len(courses))
print(courses[0])

# get the last item
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

# print(help(list))

# add item to end of list
courses.append('art')
print(courses)

# add item to specific location of list
courses.insert(1, 'geography')
print(courses)

# add using extend (when you want to add multiple values)
courses2 = ['abc', 'efg']
# courses.append(courses2)
# print(courses) # returns wrong result
courses.extend(courses2)
print(courses)

# remove values from list
courses.remove('math')
print(courses)
last_element = courses.pop() # removes last value from list and returns it
print(last_element)
print(courses)

# sorting list
courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [1, 5, 4, 3]
nums.sort()
print(nums)

nums.sort(reverse = True)
print(nums)

# sorting without altering original
courses = ['history', 'math', 'physics', 'compsci']
sorted_corsers = sorted(courses)
print(courses)
print(sorted_corsers)

# min max and sum from list
print(min(nums))
print(max(nums))
print(sum(nums))

# find index of certain value in list
print(courses.index('compsci'))
# print(courses.index('xyz')) # will throw an error if value does not exists
print('Art' in courses)
print('math' in courses)

for i, course in enumerate(courses, start=1):
	print(i, course)

# convert list to a string
course_str = ', '.join(courses)
print(course_str)

# convert string into list
new_list = course_str.split(', ')
print(new_list)

# TUPLES
# We cannot modify tupes they are immutable
print("=============TUPLES=============")

# Mutable
# list_1 = ['history', 'math', 'physics', 'compsci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)

# Immutable
tuple_1 = ('history', 'math', 'physics', 'compsci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' # this will throw an error

print(tuple_1)
print(tuple_2)

# SETS
print("=============SETS=============")

cs_courses = {'history', 'math', 'physics', 'compsci'}
print(cs_courses)

cs_courses = {'history', 'math', 'physics', 'compsci', 'math'}
print(cs_courses)

print('Math' in cs_courses) # this is faster in sets

cs_courses = {'history', 'math', 'physics', 'compsci'}
art_courses = {'history', 'art', 'design', 'compsci'}

# inner join
print(cs_courses.intersection(art_courses))

# anti join
print(cs_courses.difference)

# union
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This is not right! This is a dictionary
empty_set = set() # Proper way


