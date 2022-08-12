mystr="Devansh is a good boy"
print(len(mystr))
print(mystr[0:5])#this is know as string slicing
print(mystr[0::2])#this is advanced string slicing by default the value is 1 but if specifies the value it print the string by cutting the value
print(mystr[::])#if you dont give any it will print the whole value
print(mystr[-3:])
print(mystr[::-1])#this will reverse the string
print(mystr[::-2])#this will reverse the string and print with the gap of 2
print(mystr.isalpha())#this will the spaces
print(mystr.endswith('y'))
print("Enter value to count its repetion")
findvalue=input()

print(mystr.count(findvalue))
print(mystr.capitalize())
print(mystr.upper())
print(mystr.replace("is","are"))