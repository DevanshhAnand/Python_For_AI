# it tells the information of the object ex- how it is stored what types of it is etc etc...
# exp-type function type(var)

import email
from traceback import print_tb


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property#To make email for fname and lname
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter#This is to fetch name from email and change email attribute
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter#This is to delete attribute
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("skill","f")
print(type(skillf))
print(dir(skillf))
o="This is string"
print(dir(o))#this will show the functions which we can perform
print(id(skillf))#this is unique
print(type("This is string"))
print(id("This is string"))

import inspect
print(inspect.getmembers(skillf))