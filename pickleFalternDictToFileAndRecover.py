import pickle

dt = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
w = open("test.pkl", "wb")
pickle.dump(dt, w)
w.close()

r = open("test.pkl", "rb")
td = pickle.load(r)
print(td)