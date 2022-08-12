# set is same like list and dictionary but the difference is it stores distinct value
# means you can't store same value

s=set()
s.add(3)
s.add(4)
s.intersection({1,2,3})
print(s)

print(min(s))