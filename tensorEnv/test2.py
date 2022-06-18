import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model, preprocessing
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
data = pd.read_csv("cal.csv",sep=",")



data = data[["age","weight(kg)","height(cm)","gender","activity_level","calories_to_maintain_weight"]]


predict ="calories_to_maintain_weight"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
best = 0
for _ in range(100):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
    print(_)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    if acc > best:
        best = acc
        with open("calmodel.pickle", "wb") as f:
            pickle.dump(linear, f)

print(best)

'''
pickle_in = open("calmodel2.pickle", "rb")
linear = pickle.load(pickle_in)
value = [["49","85","1.63","1","32.2"]]

print("coefficient:\n", + linear.coef_)
print("Intercept:\n", + linear.intercept_)

predictions = linear.predict(value)
for x in range (len(predictions)):
   print(predictions)

p = 'height(new)'
style.use("ggplot")

pyplot.scatter(data[p], data["calories_to_maintain_weight"])

pyplot.xlabel(p)

pyplot.ylabel("Final cal")

pyplot.show()
'''