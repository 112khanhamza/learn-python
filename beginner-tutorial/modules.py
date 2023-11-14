import my_module as mm

courses = ['history', 'math', 'art', 'compsci']

index = mm.find_index(courses, 'math')
print(index)

# from my_module import find_index, test

# courses = ['history', 'math', 'art', 'compsci']

# index = find_index(courses, 'math')
# print(index)
# print(test)

# from my_module import find_index as fi, test

# courses = ['history', 'math', 'art', 'compsci']

# index = fi(courses, 'math')
# print(index)
# print(test)


## Importing everything ## Should not use
# from my_module import *

# courses = ['history', 'math', 'art', 'compsci']

# index = find_index(courses, 'math')
# print(index)
# print(test)

# import sys
# sys.path.append('/Users/hamzakhan/Desktop/My-Module')

# from my_module import find_index as fi, test

# courses = ['history', 'math', 'art', 'compsci']

# index = fi(courses, 'math')
# # print(index)
# # print(test)
# print(sys.path)

# Pyhton standard library
import random

courses = ['history', 'math', 'art', 'compsci']
random_course = random.choice(courses)
print(random_course)

import math

rads = math.radians(90)
print(rads)

print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

import os

print(os.getcwd())
print(os.__file__)

# import antigravity
