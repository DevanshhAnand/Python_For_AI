import pickle

# pickling a python object
cars=["Audi","BMW","Maruti suzuki"]
file='mycars.pkl'
fileobj=open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close()



file = "mycars.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
