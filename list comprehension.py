# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# # lsit comprehension
# lscomprehension=[i for i in range(100) if i%3==0]
# print(lscomprehension)

# # dictionary comprehension
# dict1 ={i:f"item{i}"for i in range(100)}
# # to swap key and value
# dict1={value:key for key,value in dict1.items()}
# print(dict1)

# # set comprehensions
# dresses={dress for dress in ["dress1","dress2","dress3","dress3","dress2"]}
# print(dresses)

# evens = (i for i in range(100) if i%2==0)
# print(type(evens))
# print(evens.__next__())

from numpy import append


n = int(input("enter the no. of elements: "))
lis=[]
for i in range(n):
    i = int(input("Enter elements: "))
    lis.append(i)

print(lis)

print("1.list comprehension \n2.dictionary comprehension\n3.set comprehension\nEnter which comprehension you want to perform: ",end="")
userop=input()
if userop=='dictionary':
    dict1 ={i:f"item{i}"for i in lis}
    print(dict1)

elif userop=='set':
    dresses={dress for dress in lis}
    print(dresses)

elif userop=='list':
    lscomprehension=[i for i in lis]
    print(lscomprehension)