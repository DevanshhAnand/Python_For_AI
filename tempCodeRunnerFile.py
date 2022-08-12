cars=["Audi","BMW","Maruti suzuki"]
file='mycars.pkl'
fileobj=open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close()