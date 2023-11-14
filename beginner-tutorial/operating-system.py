import os

# gets current working directory
print(os.getcwd())

# navigate to desktop
# Change directory
os.chdir('/Users/hamzakhan/Desktop')

print(os.getcwd())

# print files inside directory
print(os.listdir())

# create folder
# os.mkdir('os-folder')

# # create nested directories
# os.makedirs('os-folder/test/test1')

# print(os.listdir())

# os.rmdir('os-folder')

os.removedirs('os-folder/test/test1')

# rename file
