# f = open("trial.txt","rt")
# print(f.readlines())
# f.close()

with open("trial.txt") as f:
    a = f.readlines(4)
    print(a)

#