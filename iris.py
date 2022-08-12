
import pickle
import requests

# data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text

# l1=data.split('\n')
# # print(l1)

# l2 = [items.split(',') for items in l1 if len(items)!=0]
# print(l2)

# with open('iris.pkl','wb')as f:
#     pickle.dump(l2,f)


with open("iris.pkl","rb") as f:
    print(pickle.load(f))