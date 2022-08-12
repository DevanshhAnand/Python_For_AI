grocery = ["dal",11,"rice","flour","chicken"]
# print(grocery)
# print(grocery[1])
# numbers=[1,23232,34323,44]
# numbers.sort()
# print(numbers)
# print(numbers[1:4])#slicing
# numbers.reverse()
# numbers.append(22)
# numbers.insert(2,46456)
# numbers.remove(1)
# numbers.pop()
# print(numbers)

# mutable - can change eg-list
# immutable - can't change eg-tuple

tp = (1,2,3)
# to make sigle valued tuple
tp1=(1,)
print(tp)

# to exchange the value
a =1
b =2
print(a,b)
# normal way
temp = a
a = b
b = temp
print(a,b)
# pythonist way
a,b=b,a
print(a,b)