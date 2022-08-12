dictionary = {"mutable": ["it can be changed","changable"],
              "immutable":"it can't be changed",
              "string":"collection of characters",
              "Data structure,data structure":"it is the way of structuring data in a proper way"}

print("Enter the word to finds its meaning or definition: ",end="")
word = input()
# print(dictionary.values())
print(dictionary[word])
