import pickle

dt = {'Python' : {'C++' : {'C++' : '.cpp', 'Java' : '.java'}, 'Java' : {'C++' : '.cpp', 'Java' : '.java'}}, 'C++' : {'C++' : {'C++' : '.cpp', 'Java' : '.java'}, 'Java' : '.java'}, 'Java' : {'C++' : '.cpp', 'Java' : '.java'}}
w = open("test.pkl", "wb")
pickle.dump(dt, w)
w.close()

r = open("test.pkl", "rb")
td = pickle.load(r)
print(td)