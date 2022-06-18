
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model, preprocessing
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
'''
data = pd.read_csv("calorie.csv", sep=",")



data = data[["age","weight(kg)","gender","height(m)","BMI","calories_to_maintain_weight"]]


predict ="calories_to_maintain_weight"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

best = 0
for _ in range(10000):
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
class cal:
    def __init__(self,value):
         self.value = value

    def fun(value):
         pickle_in = open("tensorEnv/calmodel.pickle", "rb")
         linear = pickle.load(pickle_in)

         '''
         print("coefficient:\n", + linear.coef_)
         
         print("Intercept:\n", + linear.intercept_)
         '''
         predictions = linear.predict(value)
         k = predictions[0]
         print(k)

         return k
    
    def Bmi(bmi):
        if bmi<18.5 :
            a = "your in stage of under weight"
            b=1
        if 18.5<bmi<24.9 :
            a = "your in stage of normal weight"
            b = 2
        if 25<bmi<29.9 :
            a = "your in stage ofover weight"
            b=0
        if 30<bmi<34.9 :
            a = "your in stage of OBESE weight"
            b=0
        if 30<bmi>34.9 :
            a = "your in stage of Extremely Obese"
            b=0   
        return a,b

    def get_pro_car_fat(cal):
        get=[]
        protein1 =int((15*cal/100)/4)
        protein2= int((25 * cal / 100) / 4)
        print("protein g to take :-" ,protein1,"to",protein2," g")
        get.append([protein1,protein2])

        carbohy1=int((45*cal/100)/4)
        carbohy2= int((65 * cal / 100) / 4)
        print("carbo g to take :- ",carbohy1,"to",carbohy1," g")
        get.append([carbohy1,carbohy2])

        fat1 =int((20*cal/100)/9)
        fat2= int((35 * cal / 100) / 9)
        print("fat g to take :- ",fat1,"to",fat2," g")
        get.append([fat1,fat2])

        print("---------------------------------------------------------------------------------")
        return(get)

    def break_lunch_dinner(cal):
        get = []
        print("eat three meals a day")

        print(" moring 7 a.m.")
        break1 = int(30*cal/100)
        break2 = int(36 * cal / 100)
        print("cal to take in break :-",break1,"to",break2," cal")
        get.append([break1,break2])

        print(" afternoon 1 a.m.")
        lunch1=int(35*cal/100)
        lunch2= int(41 * cal / 100)
        print("cal to take in lunch :-",lunch1,"to",lunch1," cal")
        get.append([lunch1,lunch2])

        print(" night 7 p.m.")
        dinner1 =int(27*cal/100)
        dinner2 = int(33 * cal / 100)
        print("cal to take in dinner :-",dinner1,"to",dinner2 ," cal")
        get.append([dinner1,dinner2])

        print("---------------------------------------------------------------------------------")
        return (get)

    def break_lunch_aftersnack_dinner(cal):
        get = []
        print("eat 4 meals a day")

        print(" moring 7 a.m.")
        break1 = int(27*cal/100)
        break2 = int(32 * cal / 100)
        print("cal to take in break :-",break1,"to",break2," cal")
        get.append([break1,break2])

        print(" afternoon 1 a.m.")
        lunch1=int(37*cal/100)
        lunch2= int(45 * cal / 100)
        print("cal to take in lunch :-",lunch1,"to",lunch2," cal")
        get.append([lunch1,lunch2])

        print(" evening 4 a.m.")
        asnack1 = int(5 * cal / 100)
        asnack2 = int(10 * cal / 100)
        print("cal to take in aftersnack :-", asnack1, "to", asnack2, " cal")
        get.append([asnack1,asnack2])

        print(" night 7 a.m.")
        dinner1 =int(15*cal/100)
        dinner2 = int(20 * cal / 100)
        print("cal to take in dinner :-",dinner1,"to",dinner2 ," cal")
        get.append([dinner1,dinner2])

        print("---------------------------------------------------------------------------------")
        return (get)



    def break_morsnack_lunch_aftersnack_dinner(cal):
        get = []
        print("eat 5 meals a day")

        print(" moring 7 a.m.")
        break1 = int(25*cal/100)
        break2 = int(30 * cal / 100)
        print("cal to take in break :-",break1,"to",break2," cal")
        get.append([break1,break2])

        print(" moring 10 a.m.")
        marsnack1 = int(5 * cal / 100)
        marsnack2= int(10* cal / 100)
        print("cal to take in morning snack :-", marsnack1, "to", marsnack2, " cal")
        get.append([marsnack1, marsnack2])

        print(" afternoon 1 a.m.")
        lunch1=int(35*cal/100)
        lunch2= int(40 * cal / 100)
        print("cal to take in lunch :-",lunch1,"to",lunch2," cal")
        get.append([lunch1,lunch2])

        print(" afternoon 4 a.m.")
        asnack1 = int(5 * cal / 100)
        asnack2 = int(10 * cal / 100)
        print("cal to take in aftersnack :-", asnack1, "to", asnack2, " cal")
        get.append([asnack1, asnack2])


        print(" night 7 p.m.")
        dinner1 =int(15*cal/100)
        dinner2 = int(20 * cal / 100)
        print("cal to take in dinner :-",dinner1,"to",dinner2 ," cal")
        get.append([dinner1,dinner2])

        print("---------------------------------------------------------------------------------")
        return (get)
