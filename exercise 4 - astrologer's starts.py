n=int(input("Enter no. of rows: "))
bol=int(input("Enter 1 0r 0: "))
bol2=bool(bol)
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#         for k in range(n-i,-1):
#             print(" ")
#             k = k-1
#
#         j=j+1
#     print("\n",end="")
#     i=i+1
if bol2==True:
    for i in range(1, n + 1):
        print("*" * int(i))
elif bol2==False:
    for i in range(n, 0, -1):
        print("*" * int(i))