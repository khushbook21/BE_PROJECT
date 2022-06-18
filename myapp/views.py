from cgi import test
from pyexpat.errors import messages as mess
from django.contrib import messages
from django.http import HttpResponse
from multiprocessing import context
from django import http
from django.shortcuts import render,redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime


from tensorEnv import test 
from tensorEnv import dietfood,dieinfo


from myapp.models import userform as users
from myapp.models import contact as con
from myapp.models import feedback as  feed

diseasevalue=0
usernamevalue=0




# Create your views here.


def indexbef(request):
   return render(request,'indexbef.html')
   


def handellogin(request):
     global usernamevalue
     
     if request.method == 'POST':
            logname = request.POST['logname'] 
            logpassw= request.POST['logpassword']
            # check for errorneous input
            user = authenticate(username=logname, password=logpassw)
           
            if user is not None:
               login(request,user)
               messages.success(request, " successfull Logged  In")
               #return render(request,'indexaflogin.html')
               usernamevalue=logname
               print(usernamevalue)
               #return render(request,'indexaflogin.html',context)    
               #return redirect('indexaflogin',usernamevalue)         
               return redirect('indexaflogin')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            else:
               messages.success(request, " Invalid Credential, Please try again")
               return redirect('login_register')
     return HttpResponse("errro login")

def handellogout(request):
         logout(request)
         messages.success(request, "logout seccessfull")
         return redirect('indexbef')
def indexaflogin(request):
   #context={"userval":i}
   
   #return render(request,'indexaflogin.html',context)
   return render(request,'indexaflogin.html')

def disease(request):
    return render(request,'disease.html')


def data(request):


    dataa = users.objects.filter(usernamenew=usernamevalue)
    print(usernamevalue)
    # for d in data:
    #     print(d)
    # print(data)
    li = []
    lw = []
    lj =[]
    lis = []
    userdies=[]
    print(len(dataa))
    for j in range(len(dataa)):
        if j == (len(dataa)-1):
            i=dataa[j]
            "-----------------   for calories           -----------"
            li.append(str(i.dob))
            li.append(str(i.war))
            li.append(str(i.hight))
            li.append(str(i.gender))
            lj.append(i.hight)
            lj.append(i.acti)
            lw.append(i.war)
            "----------------------for symtoms----------------------"
            
            lis.append(int(i.feeling))
            lis.append(int(i.hadache))
            lis.append(int(i.lathrgy))
            lis.append(int(i.reduce))
            lis.append(int(i.wtl))
            lis.append(int(i.dic))
            lis.append(int(i.bodypain))
            userdies.append(str(i.disease))
            userdies.append(str(i.usernamenew))
    print(li)
    print(lj)
    print(lis)
    print(userdies)
    
    print("-----------------------------------------------DISEASE---------------------------")
    
    disevalue=userdies[0]
    print(disevalue)
    fte=0
    ftni=0
    gen=0
    nonfruit=0
    vegnot=0
    nonvegnot=0


    if disevalue == "atherosclerosis" :
        ather=dieinfo.sympt.atherosclerosis(1)
       
        print("food to eat =",ather["atherosclerosis"][0]["food to eat"])
        print("")
        print("Foods to not include =",ather["atherosclerosis"][0]["food to not eat"])
        print("")
        print("general tips =",ather["atherosclerosis"][0]["general tips"])
        print("")
        print("fruitsnot =",ather["atherosclerosis"][0]["fruitsnot"])
        print("")
        print("vegnot =",ather["atherosclerosis"][0]["vegnot"])
        print("")
        print("nonvegnot =",ather["atherosclerosis"][0]["nonvegnot"])
        fte=ather["atherosclerosis"][0]["food to eat"]
        ftni=ather["atherosclerosis"][0]["food to not eat"]
        gen=ather["atherosclerosis"][0]["general tips"]
        nonfruit=ather["atherosclerosis"][0]["general tips"]
        vegnot=ather["atherosclerosis"][0]["vegnot"]
        nonvegnot=ather["atherosclerosis"][0]["nonvegnot"]
    if disevalue == "pulmonaryfibrosis":
        pul=dieinfo.sympt.pulmonaryfibrosis(1)
        
        print("food to eat =",pul["pulmonaryfibrosis"][0]["food to eat"])
        print("")
        print("Foods to not include =",pul["pulmonaryfibrosis"][0]["food to not eat"])
        print("")
        print("general tips =",pul["pulmonaryfibrosis"][0]["general tips"])
        print("")
        print("fruitsnot =",pul["pulmonaryfibrosis"][0]["general tips"])
        print("")
        print("vegnot =",pul["pulmonaryfibrosis"][0]["vegnot"])
        print("")
        print("nonvegnot",pul["pulmonaryfibrosis"][0]["nonvegnot"])
        fte=pul["pulmonaryfibrosis"][0]["food to eat"]
        ftni=pul["pulmonaryfibrosis"][0]["food to not eat"]
        gen=pul["pulmonaryfibrosis"][0]["general tips"]
        nonfruit=pul["pulmonaryfibrosis"][0]["general tips"]
        vegnot=pul["pulmonaryfibrosis"][0]["vegnot"]
        nonvegnot=pul["pulmonaryfibrosis"][0]["nonvegnot"]

    if disevalue == "covid-19":
        cov=dieinfo.sympt.covid(1)
        
        print("food to eat =",cov["covid-19"][0]["food to eat"])
        print("")
        print("Foods to not include =",cov["covid-19"][0]["food to not eat"])
        print("")
        print("general tips =",cov["covid-19"][0]["general tips"])
        print("")
        print("fruitsnot =",cov["covid-19"][0]["fruitsnot"])
        print("")
        print("vegnot =",cov["covid-19"][0]["vegnot"])
        print("")
        print("nonvegnot =",cov["covid-19"][0]["nonvegnot"])  
        fte=cov["covid-19"][0]["food to eat"]
        ftni=cov["covid-19"][0]["food to not eat"]
        gen=cov["covid-19"][0]["general tips"]
        nonfruit=cov["covid-19"][0]["general tips"]
        vegnot=cov["covid-19"][0]["vegnot"]
        nonvegnot=cov["covid-19"][0]["nonvegnot"]
    if disevalue ==  "liver":
        liv=dieinfo.sympt.liverdisorders(1)
        
        print("food to eat =",liv["liver"][0]["food to eat"])
        print("")
        print("Foods to not include =",liv["liver"][0]["food to not eat"])
        print("")
        print("general tips =",liv["liver"][0]["general tips"])
        print("")
        print("fruitsnot =",liv["liver"][0]["fruitsnot"])
        print("")
        print("vegnot =",liv["liver"][0]["vegnot"])
        print("")
        print("nonvegnot =",liv["liver"][0]["nonvegnot"])
        fte=liv["liver"][0]["food to eat"]
        ftni=liv["liver"][0]["food to not eat"]
        gen=liv["liver"][0]["general tips"]
        nonfruit=liv["liver"][0]["general tips"]
        vegnot=liv["liver"][0]["vegnot"]
        nonvegnot=liv["liver"][0]["nonvegnot"]
    if disevalue == "pancreatic":
        panc=dieinfo.sympt.pancreatic(1)        
        
        print("food to eat = ",panc["pancreatic"][0]["food to eat"])
        print("")
        print("Foods to not include = ",panc["pancreatic"][0]["food to not eat"])
        print("")
        print("general tips",panc["pancreatic"][0]["general tips"])
        print("")
        print("fruits not = ",panc["pancreatic"][0]["fruitsnot"])
        print("")
        print("veg not = ",panc["pancreatic"][0]["vegnot"])
        print("")
        print("nonveg not = ",panc["pancreatic"][0]["nonvegnot"])
        print("")
        fte=panc["pancreatic"][0]["food to eat"]
        ftni=panc["pancreatic"][0]["food to not eat"]
        gen=panc["pancreatic"][0]["general tips"]
        nonfruit=panc["pancreatic"][0]["general tips"]
        vegnot=panc["pancreatic"][0]["vegnot"]
        nonvegnot=panc["pancreatic"][0]["nonvegnot"]
    if disevalue == "bloodcancer":
        blo=dieinfo.sympt.bloodcancer(1)
        print("food to eat =",blo["bloodcancer"][0]["food to eat"])
        print("")
        print("Foods to not include =",blo["bloodcancer"][0]["food to not eat"])
        print("")
        print("general tips =",blo["bloodcancer"][0]["general tips"])
        print("")
        print("fruitsnot =",blo["bloodcancer"][0]["fruitsnot"])
        print("")
        print("vegnot  =",blo["bloodcancer"][0]["vegnot"])
        print("")
        print("nonvegnot =",blo["bloodcancer"][0]["nonvegnot"])
        print("")
        fte=blo["bloodcancer"][0]["food to eat"]
        ftni=blo["bloodcancer"][0]["food to not eat"]
        gen=blo["bloodcancer"][0]["general tips"]
        nonfruit=blo["bloodcancer"][0]["general tips"]
        vegnot=blo["bloodcancer"][0]["vegnot"]
        nonvegnot=blo["bloodcancer"][0]["nonvegnot"]
    if disevalue == "thyroid":
        thy=dieinfo.sympt.thyroid(1) 
        print("food to eat =",thy["thyroid"][0]["food to eat"])
        print("")
        print("Foods to not include =",thy["thyroid"][0]["food to not eat"])
        print("")
        print("general tips =",thy["thyroid"][0]["general tips"])
        print("")
        print("fruitsnot =",thy["thyroid"][0]["fruitsnot"])
        print("")
        print("vegnot  =",thy["thyroid"][0]["vegnot"])
        print("")
        print("nonvegnot =",thy["thyroid"][0]["nonvegnot"])
        print("")
        fte=thy["thyroid"][0]["food to eat"]
        ftni=thy["thyroid"][0]["food to not eat"]
        gen=thy["thyroid"][0]["general tips"]
        nonfruit=thy["thyroid"][0]["general tips"]
        vegnot=thy["thyroid"][0]["vegnot"]
        nonvegnot=thy["thyroid"][0]["nonvegnot"]

    print("")
    print("-----------------------------------------------symtoms---------------------------")
    activityLevel=lj[1]
  
    print(activityLevel)
    print("")
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
    
   
    actval=str(activityLevelIndex)
    print(activityLevelIndex)
    
   

    valuesent=[]
    height=lj[0]
    weight=lw[0]
    h=height/100
    bmi=weight/(h*h)
    li.append(actval)
    valuesent.append(li)
    val = int(test.cal.fun(valuesent))  
    print("")
    print("Calories requried",int(val))
    print("")
    pcf = test.cal.get_pro_car_fat(val)
    print(pcf)
    dietplan3 = test.cal.break_lunch_dinner(val)
    print(dietplan3)
    dietplan4 = test.cal.break_lunch_aftersnack_dinner(val)
    print(dietplan4)
    dietplan5 = test.cal.break_morsnack_lunch_aftersnack_dinner(val)
    print(dietplan5)
    sym = dietfood.dfood(lis)
    s=sym.food()  
    print(s)
   
    bmi2=test.cal.Bmi(bmi)
    print(bmi2)
    print(bmi)


    '''--------------------------------exp yoga---------------------------------------------------------'''
    
    if  bmi2[1]==1:
        ex1="Squats"
        ex2="Push-Ups"
        ex3="Bench Dips."
        ex4="Lunges"
        ex5="Crunches"
        ex6="Glute Kickback"
        yoga1="Supta Badhakonasana (Reclining butterfly pose)"
        yoga2="Vajrasana (Diamond pose, Thunderbolt pose)"
        yoga3="Sarvangasana (Shoulder stand pose)"
        yoga4="Bhujangasana (Cobra pose)"
        yoga5="Matsyasana (Fish pose)"
        yoga6="Dhanurasana."
        wedis="you need to again your weight"
    elif bmi2[1]==2:
        ex1="Weight training"
        ex2="Interval training."
        ex3="Cycling"
        ex4="Glute Kickback"
        ex5="Pilates"
        ex6="Bench Dips"
        yoga1="Bhujangasana (Cobra pose)"
        yoga2="Dhanurasana (Bow pose)"
        yoga3="Kumbhakasana (The plank)"
        yoga4="Naukasana (Boat pose)"
        yoga5="Ustrasana (Camel Pose)"
        yoga6="Matsyasana (Fish pose)"
        wedis="you need to Maintain your weight"
    elif bmi2[1]==0:
        print(0)   
        ex1="Walking"
        ex2="Jogging or running"
        ex3="Cycling"
        ex4="Swimming."
        ex5="Pilates"
        ex6="Jump rope"

        yoga1="Virabhadrasana(Warrior Pose)"
        yoga2="Trikonasana(Triangle pose)"
        yoga3="Adho Mukha Svanasana(Downward Dog pose)"
        yoga4="Sarvangasana(Shoulder Stand Pose)"
        yoga5="Sethu Bandha Sarvangasana(Bridge pose)"
        yoga6="Parivrtta Utkatasana(Twisted Chair pose)"
        wedis="you need to lose your weight"
        

    
    '''---------------------------------------------------------------------------------------------'''
    context={"fte":fte[0],
    "ftni":ftni[0],
    "gen":gen[0],
    "nonfruit":nonfruit[0],
    "vegnot":vegnot[0],
    "nonvegnot":nonvegnot[0],
    "wedis":wedis,
     "user":userdies[1],
     
    "Ex1":ex1,"Ex2":ex2,"Ex3":ex3,"Ex4":ex4,"Ex5":ex5,"Ex6":ex6,
    "Yoga1":yoga1,"Yoga2":yoga2,"Yoga3":yoga3,"Yoga4":yoga4,"Yoga5":yoga5,"Yoga6":yoga6,
    "fru":s[1],"vit":s[0],"veg":s[2],"nonveg":s[3],"gena":s[4],"other":s[5],"weival": bmi2[0] , "die":userdies[0],"cal":val,"pro1":pcf[0][0],"car1":pcf[1][0],"fat1":pcf[2][0],"pro2":pcf[0][1],"car2":pcf[1][1],"fat2":pcf[2][1],"break1":dietplan3[0][0],"lunch1":dietplan3[1][0],"dinner1":dietplan3[2][0],"break11":dietplan3[0][1],"lunch11":dietplan3[1][1],"dinner11":dietplan3[2][1],"break2":dietplan4[0][0],"lunch2":dietplan4[1][0],"afsnack":dietplan4[2][0],"dinner2":dietplan4[3][0],"break21":dietplan4[0][1],"lunch21":dietplan4[1][1],"afsnack1":dietplan4[2][1],"dinner21":dietplan4[3][1],"break3":dietplan5[0][0],"morsnack":dietplan5[1][0],"lunch3":dietplan5[2][0],"afsnack3":dietplan5[3][0],"dinner3":dietplan5[4][0],"break31":dietplan5[0][1],"morsnack1":dietplan5[1][1],"lunch31":dietplan5[2][1],"afsnack31":dietplan5[3][1],"dinner31":dietplan5[4][1]}

    
    '''---------------------------------------symtoms----------------------------------------''' 
    
    
   
    '''-------------------------------------------------------------------------------------''' 

    return render(request,'resultpage.html',context)




def dashdata(request,i,j):


    dataa= users.objects.filter(usernamenew=j,date=i)
    

    print(usernamevalue)
    # for d in data:
    #     print(d)
    # print(data)
    li = []
    lw = []
    lj =[]
    lis = []
    userdies=[]
    print(len(dataa))
    for j in range(len(dataa)):
        if j == (len(dataa)-1):
            i=dataa[j]
            "-----------------   for calories           -----------"
            li.append(str(i.dob))
            li.append(str(i.war))
            li.append(str(i.hight))
            li.append(str(i.gender))
            lj.append(i.hight)
            lj.append(i.acti)
            lw.append(i.war)
            "----------------------for symtoms----------------------"
            
            lis.append(int(i.feeling))
            lis.append(int(i.hadache))
            lis.append(int(i.lathrgy))
            lis.append(int(i.reduce))
            lis.append(int(i.wtl))
            lis.append(int(i.dic))
            lis.append(int(i.bodypain))
            userdies.append(str(i.disease))
            userdies.append(str(i.usernamenew))

    print(li)
    print(lj)
    print(lis)
    print(userdies)
    
    print("-----------------------------------------------DISEASE---------------------------")
    
    disevalue=userdies[0]
    print(disevalue)
    fte=0
    ftni=0
    gen=0
    nonfruit=0
    vegnot=0
    nonvegnot=0


    if disevalue == "atherosclerosis" :
        ather=dieinfo.sympt.atherosclerosis(1)
       
        print("food to eat =",ather["atherosclerosis"][0]["food to eat"])
        print("")
        print("Foods to not include =",ather["atherosclerosis"][0]["food to not eat"])
        print("")
        print("general tips =",ather["atherosclerosis"][0]["general tips"])
        print("")
        print("fruitsnot =",ather["atherosclerosis"][0]["fruitsnot"])
        print("")
        print("vegnot =",ather["atherosclerosis"][0]["vegnot"])
        print("")
        print("nonvegnot =",ather["atherosclerosis"][0]["nonvegnot"])
        fte=ather["atherosclerosis"][0]["food to eat"]
        ftni=ather["atherosclerosis"][0]["food to not eat"]
        gen=ather["atherosclerosis"][0]["general tips"]
        nonfruit=ather["atherosclerosis"][0]["general tips"]
        vegnot=ather["atherosclerosis"][0]["vegnot"]
        nonvegnot=ather["atherosclerosis"][0]["nonvegnot"]
    if disevalue == "pulmonaryfibrosis":
        pul=dieinfo.sympt.pulmonaryfibrosis(1)
        
        print("food to eat =",pul["pulmonaryfibrosis"][0]["food to eat"])
        print("")
        print("Foods to not include =",pul["pulmonaryfibrosis"][0]["food to not eat"])
        print("")
        print("general tips =",pul["pulmonaryfibrosis"][0]["general tips"])
        print("")
        print("fruitsnot =",pul["pulmonaryfibrosis"][0]["general tips"])
        print("")
        print("vegnot =",pul["pulmonaryfibrosis"][0]["vegnot"])
        print("")
        print("nonvegnot",pul["pulmonaryfibrosis"][0]["nonvegnot"])
        fte=pul["pulmonaryfibrosis"][0]["food to eat"]
        ftni=pul["pulmonaryfibrosis"][0]["food to not eat"]
        gen=pul["pulmonaryfibrosis"][0]["general tips"]
        nonfruit=pul["pulmonaryfibrosis"][0]["general tips"]
        vegnot=pul["pulmonaryfibrosis"][0]["vegnot"]
        nonvegnot=pul["pulmonaryfibrosis"][0]["nonvegnot"]

    if disevalue == "covid-19":
        cov=dieinfo.sympt.covid(1)
        
        print("food to eat =",cov["covid-19"][0]["food to eat"])
        print("")
        print("Foods to not include =",cov["covid-19"][0]["food to not eat"])
        print("")
        print("general tips =",cov["covid-19"][0]["general tips"])
        print("")
        print("fruitsnot =",cov["covid-19"][0]["fruitsnot"])
        print("")
        print("vegnot =",cov["covid-19"][0]["vegnot"])
        print("")
        print("nonvegnot =",cov["covid-19"][0]["nonvegnot"])  
        fte=cov["covid-19"][0]["food to eat"]
        ftni=cov["covid-19"][0]["food to not eat"]
        gen=cov["covid-19"][0]["general tips"]
        nonfruit=cov["covid-19"][0]["general tips"]
        vegnot=cov["covid-19"][0]["vegnot"]
        nonvegnot=cov["covid-19"][0]["nonvegnot"]
    if disevalue ==  "liver":
        liv=dieinfo.sympt.liverdisorders(1)
        
        print("food to eat =",liv["liver"][0]["food to eat"])
        print("")
        print("Foods to not include =",liv["liver"][0]["food to not eat"])
        print("")
        print("general tips =",liv["liver"][0]["general tips"])
        print("")
        print("fruitsnot =",liv["liver"][0]["fruitsnot"])
        print("")
        print("vegnot =",liv["liver"][0]["vegnot"])
        print("")
        print("nonvegnot =",liv["liver"][0]["nonvegnot"])
        fte=liv["liver"][0]["food to eat"]
        ftni=liv["liver"][0]["food to not eat"]
        gen=liv["liver"][0]["general tips"]
        nonfruit=liv["liver"][0]["general tips"]
        vegnot=liv["liver"][0]["vegnot"]
        nonvegnot=liv["liver"][0]["nonvegnot"]
    if disevalue == "pancreatic":
        panc=dieinfo.sympt.pancreatic(1)        
        
        print("food to eat = ",panc["pancreatic"][0]["food to eat"])
        print("")
        print("Foods to not include = ",panc["pancreatic"][0]["food to not eat"])
        print("")
        print("general tips",panc["pancreatic"][0]["general tips"])
        print("")
        print("fruits not = ",panc["pancreatic"][0]["fruitsnot"])
        print("")
        print("veg not = ",panc["pancreatic"][0]["vegnot"])
        print("")
        print("nonveg not = ",panc["pancreatic"][0]["nonvegnot"])
        print("")
        fte=panc["pancreatic"][0]["food to eat"]
        ftni=panc["pancreatic"][0]["food to not eat"]
        gen=panc["pancreatic"][0]["general tips"]
        nonfruit=panc["pancreatic"][0]["general tips"]
        vegnot=panc["pancreatic"][0]["vegnot"]
        nonvegnot=panc["pancreatic"][0]["nonvegnot"]
    if disevalue == "bloodcancer":
        blo=dieinfo.sympt.bloodcancer(1)
        print("food to eat =",blo["bloodcancer"][0]["food to eat"])
        print("")
        print("Foods to not include =",blo["bloodcancer"][0]["food to not eat"])
        print("")
        print("general tips =",blo["bloodcancer"][0]["general tips"])
        print("")
        print("fruitsnot =",blo["bloodcancer"][0]["fruitsnot"])
        print("")
        print("vegnot  =",blo["bloodcancer"][0]["vegnot"])
        print("")
        print("nonvegnot =",blo["bloodcancer"][0]["nonvegnot"])
        print("")
        fte=blo["bloodcancer"][0]["food to eat"]
        ftni=blo["bloodcancer"][0]["food to not eat"]
        gen=blo["bloodcancer"][0]["general tips"]
        nonfruit=blo["bloodcancer"][0]["general tips"]
        vegnot=blo["bloodcancer"][0]["vegnot"]
        nonvegnot=blo["bloodcancer"][0]["nonvegnot"]
    if disevalue == "thyroid":
        thy=dieinfo.sympt.thyroid(1) 
        print("food to eat =",thy["thyroid"][0]["food to eat"])
        print("")
        print("Foods to not include =",thy["thyroid"][0]["food to not eat"])
        print("")
        print("general tips =",thy["thyroid"][0]["general tips"])
        print("")
        print("fruitsnot =",thy["thyroid"][0]["fruitsnot"])
        print("")
        print("vegnot  =",thy["thyroid"][0]["vegnot"])
        print("")
        print("nonvegnot =",thy["thyroid"][0]["nonvegnot"])
        print("")
        fte=thy["thyroid"][0]["food to eat"]
        ftni=thy["thyroid"][0]["food to not eat"]
        gen=thy["thyroid"][0]["general tips"]
        nonfruit=thy["thyroid"][0]["general tips"]
        vegnot=thy["thyroid"][0]["vegnot"]
        nonvegnot=thy["thyroid"][0]["nonvegnot"]

    print("")
    print("-----------------------------------------------symtoms---------------------------")
    activityLevel=lj[1]
  
    print(activityLevel)
    print("")
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
    
   
    actval=str(activityLevelIndex)

    bmi2=test.cal.Bmi(activityLevelIndex)
    print("BMI",bmi2) 
    print("")

    valuesent=[]
    height=lj[0]
    weight=lw[0]
    h=height/100
    bmi=weight/(h*h)
    li.append(actval)
    valuesent.append(li)
    val = int(test.cal.fun(valuesent))  
    print("")
    print("Calories requried",int(val))
    print("")
    pcf = test.cal.get_pro_car_fat(val)
    print(pcf)
    dietplan3 = test.cal.break_lunch_dinner(val)
    print(dietplan3)
    dietplan4 = test.cal.break_lunch_aftersnack_dinner(val)
    print(dietplan4)
    dietplan5 = test.cal.break_morsnack_lunch_aftersnack_dinner(val)
    print(dietplan5)
    sym = dietfood.dfood(lis)
    s=sym.food()  
    print(s)
   



    '''--------------------------------exp yoga---------------------------------------------------------'''
    
    if  bmi2[1]==1:
        ex1="Squats"
        ex2="Push-Ups"
        ex3="Bench Dips."
        ex4="Lunges"
        ex5="Crunches"
        ex6="Glute Kickback"
        yoga1="Supta Badhakonasana (Reclining butterfly pose)"
        yoga2="Vajrasana (Diamond pose, Thunderbolt pose)"
        yoga3="Sarvangasana (Shoulder stand pose)"
        yoga4="Bhujangasana (Cobra pose)"
        yoga5="Matsyasana (Fish pose)"
        yoga6="Dhanurasana."
        wedis="you need to again your weight"
    elif bmi2[1]==2:
        ex1="Weight training"
        ex2="Interval training."
        ex3="Cycling"
        ex4="Glute Kickback"
        ex5="Pilates"
        ex6="Bench Dips"
        yoga1="Bhujangasana (Cobra pose)"
        yoga2="Dhanurasana (Bow pose)"
        yoga3="Kumbhakasana (The plank)"
        yoga4="Naukasana (Boat pose)"
        yoga5="Ustrasana (Camel Pose)"
        yoga6="Matsyasana (Fish pose)"
        wedis="you need to Maintain your weight"
    elif bmi2[1]==0:
        print(0)   
        ex1="Walking"
        ex2="Jogging or running"
        ex3="Cycling"
        ex4="Swimming."
        ex5="Pilates"
        ex6="Jump rope"

        yoga1="Virabhadrasana(Warrior Pose)"
        yoga2="Trikonasana(Triangle pose)"
        yoga3="Adho Mukha Svanasana(Downward Dog pose)"
        yoga4="Sarvangasana(Shoulder Stand Pose)"
        yoga5="Sethu Bandha Sarvangasana(Bridge pose)"
        yoga6="Parivrtta Utkatasana(Twisted Chair pose)"
        wedis="you need to lose your weight"
    '''--------------------------------------------'''  
    '''
    if 



    '''

    
    '''---------------------------------------------------------------------------------------------'''
    context={"fte":fte[0],
    "ftni":ftni[0],
    "gen":gen[0],
    "nonfruit":nonfruit[0],
    "vegnot":vegnot[0],
    "nonvegnot":nonvegnot[0],
    "wedis":wedis,
    "user":userdies[1],
     
    "Ex1":ex1,"Ex2":ex2,"Ex3":ex3,"Ex4":ex4,"Ex5":ex5,"Ex6":ex6,
    "Yoga1":yoga1,"Yoga2":yoga2,"Yoga3":yoga3,"Yoga4":yoga4,"Yoga5":yoga5,"Yoga6":yoga6,
    "fru":s[1],"vit":s[0],"veg":s[2],"nonveg":s[3],"gena":s[4],"other":s[5],"weival": bmi2[0] , "die":userdies[0],"cal":val,"pro1":pcf[0][0],"car1":pcf[1][0],"fat1":pcf[2][0],"pro2":pcf[0][1],"car2":pcf[1][1],"fat2":pcf[2][1],"break1":dietplan3[0][0],"lunch1":dietplan3[1][0],"dinner1":dietplan3[2][0],"break11":dietplan3[0][1],"lunch11":dietplan3[1][1],"dinner11":dietplan3[2][1],"break2":dietplan4[0][0],"lunch2":dietplan4[1][0],"afsnack":dietplan4[2][0],"dinner2":dietplan4[3][0],"break21":dietplan4[0][1],"lunch21":dietplan4[1][1],"afsnack1":dietplan4[2][1],"dinner21":dietplan4[3][1],"break3":dietplan5[0][0],"morsnack":dietplan5[1][0],"lunch3":dietplan5[2][0],"afsnack3":dietplan5[3][0],"dinner3":dietplan5[4][0],"break31":dietplan5[0][1],"morsnack1":dietplan5[1][1],"lunch31":dietplan5[2][1],"afsnack31":dietplan5[3][1],"dinner31":dietplan5[4][1]}

    
    '''---------------------------------------symtoms----------------------------------------''' 
    
    
   
    '''-------------------------------------------------------------------------------------''' 

    return render(request,'resultpage.html',context)














def dashboard(request):
 
    li = []
    lw = []
    lj =[]
    lis = []
    userdies=[]

    dataa = users.objects.filter(usernamenew=usernamevalue)
    # for d in data:
    #     print(d)
    # print(data)
    print(len(dataa))

    if len(dataa) > 0:
        for j in range(len(dataa)):
            if j == (len(dataa)-1):
                i=dataa[j]
                "-----------------   for calories           -----------"
                li.append(str(i.dob))
                li.append(str(i.war))
                li.append(str(i.hight))
                li.append(str(i.gender))
                lj.append(i.hight)
                lj.append(i.acti)
                lw.append(i.war)
                "----------------------for symtoms----------------------"
                
                lis.append(int(i.feeling))
                lis.append(int(i.hadache))
                lis.append(int(i.lathrgy))
                lis.append(int(i.reduce))
                lis.append(int(i.wtl))
                lis.append(int(i.dic))
                lis.append(int(i.bodypain))
                userdies.append(str(i.disease))
                userdies.append(str(i.usernamenew))
        print(li)
        print(lj)
        print(lis)
        print(userdies)
        
        print("-----------------------------------------------DISEASE---------------------------")
        
        disevalue=userdies[0]
        fte=0
        ftni=0
        gen=0
        nonfruit=0
        vegnot=0
        nonvegnot=0


    
        print("")
        print("-----------------------------------------------symtoms---------------------------")
        activityLevel=lj[1]
    
        print(activityLevel)
        print("")
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
        
    
        actval=str(activityLevelIndex)

        bmi2=test.cal.Bmi(activityLevelIndex)
        print("BMI",bmi2) 
        print("")

        valuesent=[]
        height=lj[0]
        weight=lw[0]
        h=height/100
        bmi=weight/(h*h)
        li.append(actval)
        valuesent.append(li)
        val = int(test.cal.fun(valuesent))  
        print("")
        print("Calories requried",int(val))
        print("")
        pcf = test.cal.get_pro_car_fat(val)
        print(pcf)
        dietplan3 = test.cal.break_lunch_dinner(val)
        print(dietplan3)
        dietplan4 = test.cal.break_lunch_aftersnack_dinner(val)
        print(dietplan4)
        dietplan5 = test.cal.break_morsnack_lunch_aftersnack_dinner(val)
        print(dietplan5)
        sym = dietfood.dfood(lis)
        s=sym.food()  
        print(s)
        if bmi2[1]==1:
            weival="you need to gain weight "
        elif bmi2[1]==2:
            weival="you need to maintain weight "
        elif bmi2[1]==0:
            weival="you need to lose weight "
        '''--------------------------------exp yoga---------------------------------------------------------'''
        sumval=[]
        for i in lis:
            if i == 1:
                sumvalue="Feelingweaker"
                sumval.append(sumvalue)
            elif i == 2:
                sumvalue="hadache"
                sumval.append(sumvalue)
            elif i ==3:
                sumvalue="lethary"
                sumval.append(sumvalue)
            elif i ==4:
                sumvalue="Reducedappetite"
                sumval.append(sumvalue)
            elif i ==5:
                sumvalue="woundhealing"
                sumval.append(sumvalue)
            elif i ==6:
                sumvalue="Decrease in conncentration"
                sumval.append(sumvalue)
            elif i ==7:
                sumvalue="Body pain"
                sumval.append(sumvalue)
        print(sumval) 

        '''--------------------------------------------------'''
    



        '''-------------------------------------------------------------------------------------''' 
        context={"dat":dataa,"symval":sumval,"weival":weival,"wedis":bmi2[0],"die":userdies[0],"cal":val,"breakfast":dietplan4[0] ,"lunch":dietplan4[1],"snack":dietplan4[2],"Dinner":dietplan4[3],"userval": usernamevalue}
        return render(request,'dashboard.html',context)
    return render(request,'disease.html')




def feedbacklog(request):   

    if request.method =='POST':
       message = request.POST.get('message')  
       mes= feed(message = message) 
       mes.save()  
       return render(request,"indexaflogin.html")            
    return render(request,'feedbacklog.html')
def feedbacklogout(request):   

    if request.method =='POST':
       message = request.POST.get('message')  
       mes= feed(message = message) 
       mes.save()  
       return render(request,"indexbef.html")            
    return render(request,'feedbacklogout.html')

def about(request):
      return render(request,'about.html')

def contactlog(request):
   
    if request.method == 'POST':
            name        =   request.POST.get('name')
            subject     =   request.POST.get('subject')
            email       =   request.POST.get('email')
            message     =   request.POST.get('message')
            contactObject   = con(name=name, sub=subject, email=email, msg= message)
           
            contactObject.save()
            messages.success(request,"thanks for contacting us.")
            return render(request,"indexaflogin.html")  
       
    return render(request,'contactlog.html') 

def contactlogout(request):
   
    if request.method == 'POST':
            name        =   request.POST.get('name')
            subject     =   request.POST.get('subject')
            email       =   request.POST.get('email')
            message     =   request.POST.get('message')
            contactObject   = con(name=name, sub=subject, email=email, msg= message)
           
            contactObject.save()
            messages.success(request,"thanks for contacting us.")
            return render(request,"indexbef.html")  
       
    return render(request,'contactlogout.html') 









def userformdies(request,i):
    print(i)
    global diseasevalue
    diseasevalue=i
    return  render(request,"userform.html")  
    

def userform(request):
    global usernamenew
    print(diseasevalue)
    disease = diseasevalue
    usernamenew=usernamevalue
    print("ok get")
    if request.method == 'POST':
        
        dob = request.POST.get('age')  
        gender = request.POST.get('gender')
        hight = request.POST.get('height')
        wbr = request.POST.get('widthb')
        war = request.POST.get('widtha')
        acti = request.POST.get('active')
        yav = request.POST.get('veg')

        feeling = request.POST.get('weaker')
        hadache = request.POST.get('hadache')
        lathrgy = request.POST.get('lethargy')
        reduce = request.POST.get('appetite')
        wtl = request.POST.get('wound')
        dic = request.POST.get('concentration')
        loi = request.POST.get('lackofinterest')
        fsleepy = request.POST.get('sleepy')
        bodypain = request.POST.get('bodypain')
                      
        
        result = users(disease=disease,usernamenew=usernamenew,dob = dob, gender = gender, hight = hight, wbr = wbr ,
        war = war, acti = acti , yav = yav, feeling = feeling, hadache = hadache, lathrgy = lathrgy,
        reduce = reduce, wtl = wtl, dic = dic, loi = loi, fsleepy = fsleepy, bodypain = bodypain
        )
        result.save()

        cpcf=[dob,gender,hight,war,acti]
        print(cpcf)
      
        return redirect('data')  
         
   
    return render(request,'userform.html')



def login_register(request):
     if request.method == 'POST':
            name = request.POST.get('name') 
            email = request.POST.get('email')
            passw =request.POST.get('password')
            cpassw =request.POST.get('cpassword')
            print(name)
            print(email)
            print(passw)
            print(cpassw)
           
            # check for errorneous input 
            if len(name)>10:
                messages.error(request,"Username must be under 10 characters")
                return redirect("login_register")
            if passw != cpassw:
                messages.error(request,"password not match")
                return redirect("login_register")
            myuser = User.objects.create_user(name,email,passw)
            myuser.Cpassword=cpassw
            myuser.save()
            messages.success(request,"ok good created")
            return render(request,'login_register.html')
     else:
            return render(request,'login_register.html')
       

            







def testfilter(request):
    dataa = users.objects.filter(usernamenew=usernamevalue)
    print(dataa)
    print(len(dataa))
    # for d in data:
    #     print(d)
    
    li = []
    lw = []
    lj =[]
    lis = []
    userdies=[]
    print(len(dataa))
    for j in range(len(dataa)):
            i=dataa[j]
            "-----------------   for calories           -----------"
            li.append(str(i.dob))
            li.append(str(i.war))
            li.append(str(i.hight))
            li.append(str(i.gender))
            lj.append(i.hight)
            lj.append(i.acti)
            lw.append(i.war)
            "----------------------for symtoms----------------------"
            
            lis.append(int(i.feeling))
            lis.append(int(i.hadache))
            lis.append(int(i.lathrgy))
            lis.append(int(i.reduce))
            lis.append(int(i.wtl))
            lis.append(int(i.dic))
            lis.append(int(i.bodypain))
            userdies.append(str(i.disease))
            userdies.append(str(i.usernamenew))
            print(li)
            print(lj)
            print(lis)
            print(userdies)
            li = []
            lw = []
            lj =[]
            lis = []
            userdies=[]
    
    
    
    return HttpResponse()