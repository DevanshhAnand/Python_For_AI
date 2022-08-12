a= 9
b= 89
c = sum((a,b))

def function1(a,b):
    """This is docstring which known as comment if not written inside the fuction first line which is written in fuction as commnent is known as docstring this is used for giving warning information about the function"""

    return a+b
def function2(a,b):
    return int((a+b)/2)

x = function1(a,b)
y = function2(a,b)

print("your sum is ",x,end=" ")
print("your average of sum is ",y)
print(function1.__doc__)
