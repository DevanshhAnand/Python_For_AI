import os
# print(dir(os))
print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
print(os.listdir())
# os.mkdir("ABC")#This will make one folder
# os.makedirs("This/That")#this will make that name folder in This folder
# os.rename("names.txt","name.txt")

print(os.environ.get('Path'))
print(os.path.join("C:/","/harry.txt"))
print(os.path.exists("C://AI"))
print(os.path.isdir("C://Program files"))