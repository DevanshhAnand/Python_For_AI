f = open("trial.txt")
# print(f.tell())
print(f.readline())
f.seek(0)#this will reset the file where you specify
# print(f.tell())
print(f.readline())
# print(f.tell())
f.close()