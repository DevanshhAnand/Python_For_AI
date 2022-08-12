
import imp
import re
from time import time


print("Enter for whom you want to lock: ")
print("1 for rohan")
print("2 for harry")
print("3 for devansh")
name = int(input("Enter the value: "))
print("Enter what you want to be locked: ")
print("1 for exercise lock")
print("2 for diet lock")
operation = int(input("Enter the value: "))


def getdate():
    import datetime
    return str(datetime.datetime.now())
    
datein = getdate()
if name == 1:
    if operation == 1:
        f = open("rohan_exercise.txt", "a")
        f.write(datein)
        f.write("\n")
        f.write(input("Enter what you have done in your exercise, Rohan: "))

        f.close()
    elif operation == 2:
        f = open("rohan_diet.txt", "a")
        f.write(datein)
        f.write("\n")
        f.write(input("Enter what you have eaten in your day, Rohan: "))
        f.close()
    else:
        print("invalid error")
if name == 2:
    if operation == 1:
        f = open("harry_exercise.txt", "a")
        f.write(datein)
        f.write("\n")
        f.write(input("Enter what you have done in your exercise, harry: "))
        f.close()
    elif operation == 2:
        f = open("harry_diet.txt", "a")
        f.write(datein)
        f.write("\n")
        f.write(input("Enter what you have eaten in your day, harry: "))
        f.close()
if name == 3:
    if operation == 1:
        f = open("devansh_exercise.txt", "a")
        f.write(datein)
        f.write("\n")
        f.write(input("Enter what you have done in your exercise, devansh: "))
        f.close()
    elif operation == 2:
        f = open("devansh_diet.txt", "a")
        f.write(datein)
        f.write("\n")
        f.write(input("Enter what you have eaten in your day, devansh: "))
        f.close()
