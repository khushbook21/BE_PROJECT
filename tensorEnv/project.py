import test
import sym
import itertools



symvalue=[]
value=[]
valuesent=[]



print("------------------------------------------------------------prediction using traind model-------------------------------------------------------------------------------")
#"age","weight(kg)","gender","height(cm)","BMI","calories_to_maintain_weight"

age = int(input("enter age :-"))
weight = int(input("enter weight(kg) :-"))
height= int(input("enter height(cm):-"))
gender= int(input("for male = 1 , female = 0 :-"))
activityLevel = int(input("enter your activity level 1 to 5:"))
print("-------------------------------------------------------------------symptom phase----------------------------------------------------------------------")

feel= int(input("feeling weaker for yes(1) no(0)  :-"))
if feel == 1:
    feel2 = 1
    symvalue.append(feel2)
lethary = int(input("lethary ness for yes(1) no(0)  :-"))
if lethary==1:
    lethary2 = 3
    symvalue.append(lethary2)
headache= int(input("headache for yes(1) no(0) :-"))
if headache==1:
    headache2=2
    symvalue.append(headache2)
wound= int(input("wounds taking a long time to heal for yes(1) no(0) "))
if wound==1:
    wound2=5
    symvalue.append(wound2)
red = int(input("reduced appetite for yes(1) no(0) :-"))
if red ==1:
    red2 = 4
    symvalue.append(red2)
dec= int(input("Decrease in concentration level for yes(1) no(0) "))
if dec==1:
    dec2=6
    symvalue.append(dec2)
bod = int(input("Body pain for yes(1) no(0) :-"))
if bod==1:
    bod2 = 7
    symvalue.append(bod2)






#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
if activityLevel == 1:
        activityLevelIndex = 1.2
elif activityLevel == 2:
        activityLevelIndex = 1.375
elif activityLevel == 3:
        activityLevelIndex = 1.46
elif activityLevel == 4:
        activityLevelIndex = 1.725
elif activityLevel == 5:
        activityLevelIndex = 1.9

value.append(str(age))
value.append(str(weight))
value.append(str(height))
value.append(str(gender))
value.append(str(activityLevelIndex))
valuesent.append(value)
print(valuesent)

h=height/100
bmi=weight/(h*h)

val = test.cal.fun(valuesent)
val1=int(val)
#---------------------------------------------------------------------------------------------------------

h=height/100
bmi=weight/(h*h)
if bmi<18.5 :
    print("your in stage of under weight")
if 18.5<bmi<24.9 :
    print("your in stage of normal weight")
if 25<bmi<29.9 :
    print("your in stage ofover weight")
if 30<bmi<34.9 :
    print("your in stage of OBESE weight")
if 30<bmi>34.9 :
    print("your in stage of Extremely Obese")

#---------------------------------------------------------------------------------------------------------
print( "calories to intake in one day :-",val1)
print("-------------------------------------------------------------------------------------")








def get_pro_car_fat(cal):
    get=[]
    protein1 =int((15*cal/100)/4)
    protein2= int((25 * cal / 100) / 4)
    print("protein g to take :-" ,protein1,"to",protein2," g")
    get.append([[protein1,protein2]])

    carbohy1=int((45*cal/100)/4)
    carbohy2= int((65 * cal / 100) / 4)
    print("carbo g to take :- ",carbohy1,"to",carbohy1," g")
    get.append([[carbohy1],[carbohy2]])

    fat1 =int((20*cal/100)/9)
    fat2= int((35 * cal / 100) / 9)
    print("fat g to take :- ",fat1,"to",fat2," g")
    get.append([[fat1],[fat2]])

    print("---------------------------------------------------------------------------------")
    return(get)

def break_lunch_dinner(cal):
    get = []
    print("eat three meals a day")

    print(" moring 7 a.m.")
    break1 = int(30*cal/100)
    break2 = int(36 * cal / 100)
    print("cal to take in break :-",break1,"to",break2," cal")
    get.append([[break1],[break2]])

    print(" afternoon 1 a.m.")
    lunch1=int(35*cal/100)
    lunch2= int(41 * cal / 100)
    print("cal to take in lunch :-",lunch1,"to",lunch1," cal")
    get.append([[lunch1],[lunch2]])

    print(" night 7 p.m.")
    dinner1 =int(27*cal/100)
    dinner2 = int(33 * cal / 100)
    print("cal to take in dinner :-",dinner1,"to",dinner2 ," cal")
    get.append([[dinner1],[dinner2]])

    print("---------------------------------------------------------------------------------")
    return (get)

def break_lunch_aftersnack_dinner(cal):
    get = []
    print("eat 4 meals a day")

    print(" moring 7 a.m.")
    break1 = int(27*cal/100)
    break2 = int(32 * cal / 100)
    print("cal to take in break :-",break1,"to",break2," cal")
    get.append([[break1],[break2]])

    print(" afternoon 1 a.m.")
    lunch1=int(37*cal/100)
    lunch2= int(45 * cal / 100)
    print("cal to take in lunch :-",lunch1,"to",lunch1," cal")
    get.append([[lunch1],[lunch2]])

    print(" evening 4 a.m.")
    asnack1 = int(5 * cal / 100)
    asnack2 = int(10 * cal / 100)
    print("cal to take in aftersnack :-", asnack1, "to", asnack2, " cal")
    get.append([[asnack1], [asnack2]])

    print(" night 7 a.m.")
    dinner1 =int(15*cal/100)
    dinner2 = int(20 * cal / 100)
    print("cal to take in dinner :-",dinner1,"to",dinner2 ," cal")
    get.append([[dinner1],[dinner2]])

    print("---------------------------------------------------------------------------------")
    return (get)



def break_morsnack_lunch_aftersnack_dinner(cal):
    get = []
    print("eat 5 meals a day")

    print(" moring 7 a.m.")
    break1 = int(25*cal/100)
    break2 = int(30 * cal / 100)
    print("cal to take in break :-",break1,"to",break2," cal")
    get.append([[break1],[break2]])

    print(" moring 10 a.m.")
    marsnack1 = int(5 * cal / 100)
    marsnack2= int(10* cal / 100)
    print("cal to take in morning snack :-", marsnack1, "to", marsnack2, " cal")
    get.append([[break1], [break2]])

    print(" afternoon 1 a.m.")
    lunch1=int(35*cal/100)
    lunch2= int(40 * cal / 100)
    print("cal to take in lunch :-",lunch1,"to",lunch2," cal")
    get.append([[lunch1],[lunch2]])

    print(" afternoon 4 a.m.")
    asnack1 = int(5 * cal / 100)
    asnack2 = int(10 * cal / 100)
    print("cal to take in aftersnack :-", asnack1, "to", asnack2, " cal")
    get.append([[lunch1], [lunch2]])


    print(" night 7 p.m.")
    dinner1 =int(15*cal/100)
    dinner2 = int(20 * cal / 100)
    print("cal to take in dinner :-",dinner1,"to",dinner2 ," cal")
    get.append([[dinner1],[dinner2]])

    print("---------------------------------------------------------------------------------")
    return (get)

pro_car_fat = get_pro_car_fat(val1)
dietplan3= break_lunch_dinner(val1)
dietplan5=break_morsnack_lunch_aftersnack_dinner(val1)
dietplan4=break_lunch_aftersnack_dinner(val1)

print("----------------------------------------------------symptoms based----------------------------------------------------------------------------------")


fe = sym.sympt.feelingweaker()
he = sym.sympt.head()
le = sym.sympt.lethary()
re = sym.sympt.reducedappetite()
wo = sym.sympt.woundhealing()
de = sym.sympt.Decrease()
bo = sym.sympt.bodypain()



#name vitmain fruie non other com veg
vam = []
fruit = []
veg = []
nonv = []
other = []
common = []


for j in range(len(symvalue)):
    i=symvalue[j]

    if i == 1:

       vam.append(fe[1])
       fruit.append(fe[2])
       veg.append(fe[6])
       nonv.append(fe[3])
       other.append(fe[4])
       common.append(fe[5])

    elif i == 2:

        vam.append(he[1])
        fruit.append(he[2])
        veg.append(he[6])
        nonv.append(he[3])
        other.append(he[4])
        common.append(he[5])
    elif i == 3:

        vam.append(le[1])
        fruit.append(le[2])
        veg.append(le[6])
        nonv.append(le[3])
        other.append(le[4])
        common.append(le[5])
    elif i == 4:

        vam.append(re[1])
        fruit.append(re[2])
        veg.append(re[6])
        nonv.append(re[3])
        other.append(re[4])
        common.append(re[5])
    elif i == 5:

        vam.append(wo[1])
        fruit.append(wo[2])
        veg.append(wo[6])
        nonv.append(wo[3])
        other.append(wo[4])
        common.append(wo[5])
    elif i == 6:

        vam.append(de[1])
        fruit.append(de[2])
        veg.append(de[6])
        nonv.append(de[3])
        other.append(de[4])
        common.append(de[5])
    elif i == 7:

        vam.append(bo[1])
        fruit.append(bo[2])
        veg.append(bo[6])
        nonv.append(bo[3])
        other.append(bo[4])
        common.append(bo[5])

print("-----------------------------------------------------converting 2D to 1D ----------------symptoms based----------------------------------------------")

def oneDArray(x):
    return list(itertools.chain(*x))
vam2 = oneDArray(vam)
fruit2= oneDArray(fruit)
veg2= oneDArray(veg)
nonv2= oneDArray(nonv)
other2= oneDArray(other)
common2= oneDArray(common)


print("-----------------------------------------------------removing duplicate ----------------symptoms based----------------------------------------------")

def redupicate(x):
        res = [i for n, i in enumerate(x) if i not in x[:n]]
        return res

vam3 = redupicate(vam2)
fruit3 = redupicate(fruit2)
veg3 = redupicate(veg2)
nonv3= redupicate(nonv2)
other3= redupicate(other2)
common3 = redupicate(common2)

print("vitamins_and_minerals need to add :-",vam3)
print("")
print("")
print("fruits need to add :-",fruit3)
print("")
print("")
print("veg need to add :-",veg3)
print("")
print("")
print("non_veg need to add :-",nonv3)
print("")
print("")
print("others need to add :-",other3)
print("")
print("")
print("common need to add  :-",common3)
print("")
print("")

print('----------------------------------------------------------------diesese----------------------------------------------------------------------')






