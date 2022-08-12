# a = input("What is your name")
# b = input("How much do you earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f"Hello {a}")
# 1000 lines taking 1 hour

# c = input("Enter your name")
# try:
#     print(a)

# except Exception as e:

#     if c =="harry":
#         raise ValueError("Harry is blocked he is not allowed")

#     print("Exception handled")


# Task - Write about 2 built in exception
# EOFError
a = input("What is your name")
if a=='':
    raise EOFError("Pls give input")

print(a)

#Key error
ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
person = input('Get age for: ')
if person not in ages:
    raise KeyError("No such keys")
print(f'{person} is {ages[person]} years old.')
