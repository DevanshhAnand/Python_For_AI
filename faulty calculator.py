# print("Enter the first digit")
# val1=int(input())
# print("Enter the operation you want to perform from (+,-,*,/)")
# sym=input()
# print("Enter the second digit")
# val2=int(input())
#
# if val1==45 and val2==3 and sym=="*":
#     print("555")
# elif val1==56 and val2==9 and sym=="+":
#     print("77")
# elif val1==56 and val2==6 and sym=="/":
#     print("4")
# else:
#     if sym=="+":
#         print(val1 + val2)
#     elif sym=="-":
#         print(val1 - val2)
#     elif sym=="*":
#         print(val1 * val2)
#     elif sym=="/":
#         print(val1 / val2)
#     else:
#         print("something went wrong, please try again")
n = int(input())
i=0
while i<n:
    print(i*i)
    i += 1