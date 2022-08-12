# var1=int(input())
# var2=56
# if var1>var2:
#     print("var 1 is greater")
# elif var1==var2:
#     print("Equal")
# else:
#     print("var 2 is greater")

n=int(input())
if ((n%2) != 0):
    print("Weird")
elif ((n%2==0) and n>=2 and n<6):
    print("Not Weird")
elif ((n%2==0) and n>=6 and n<21):
    print("Weird")
elif ((n%2==0) and n>20):
    print("Not Weird")

