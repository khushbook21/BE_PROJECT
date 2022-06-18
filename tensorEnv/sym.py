''' JavaScript Object Notation '''
import json
class sympt:
  def __init__(self):
      self.run = "run"

  def head():
    a=[]
    with open('tensorEnv/sym.json') as f:
      data = json.load(f)
    value1 = data['symptoms'][2]['headache'][0]['name']
    value2 = data['symptoms'][2]['headache'][0]['vitamins_and_minerals']
    value3 = data['symptoms'][2]['headache'][0]['fruits']
    value4 = data['symptoms'][2]['headache'][0]['non_veg']
    value5 = data['symptoms'][2]['headache'][0]['others']
    value6 = data['symptoms'][2]['headache'][0]['common']
    value7 = data['symptoms'][2]['headache'][0]['veg']
    a.append(value1)
    a.append(value2)
    a.append(value3)
    a.append(value4)
    a.append(value5)
    a.append(value6)
    a.append(value7)
    return  a

  def lethary():
    a = []
    with open('tensorEnv/sym.json') as f:
      data = json.load(f)

    value1 = data['symptoms'][1]['lethary'][0]['name']
    value2 = data['symptoms'][1]['lethary'][0]['vitamins_and_minerals']
    value3 = data['symptoms'][1]['lethary'][0]['fruits']
    value4 = data['symptoms'][1]['lethary'][0]['non_veg']
    value5 = data['symptoms'][1]['lethary'][0]['others']
    value6 = data['symptoms'][1]['lethary'][0]['common']
    value7 = data['symptoms'][1]['lethary'][0]['veg']
    a.append(value1)
    a.append(value2)
    a.append(value3)
    a.append(value4)
    a.append(value5)
    a.append(value6)
    a.append(value7)
    return a
  def feelingweaker():
    a = []
    with open('tensorEnv/sym.json') as f:
      data = json.load(f)
    value1 = data['symptoms'][0]['feelingweaker'][0]['name']
    value2 = data['symptoms'][0]['feelingweaker'][0]['vitamins_and_minerals']
    value3 = data['symptoms'][0]['feelingweaker'][0]['fruits']
    value4 = data['symptoms'][0]['feelingweaker'][0]['non_veg']
    value5 = data['symptoms'][0]['feelingweaker'][0]['others']
    value6 = data['symptoms'][0]['feelingweaker'][0]['common']
    value7 = data['symptoms'][0]['feelingweaker'][0]['veg']
    a.append(value1)
    a.append(value2)
    a.append(value3)
    a.append(value4)
    a.append(value5)
    a.append(value6)
    a.append(value7)
    return a

  def woundhealing():
    a=[]
    with open('tensorEnv/sym.json') as f:
      data = json.load(f)
    value1 = data['symptoms'][3]['wound healing'][0]['name']
    value2 = data['symptoms'][3]['wound healing'][0]['vitamins_and_minerals']
    value3 = data['symptoms'][3]['wound healing'][0]['fruits']
    value4 = data['symptoms'][3]['wound healing'][0]['non_veg']
    value5 = data['symptoms'][3]['wound healing'][0]['others']
    value6 = data['symptoms'][3]['wound healing'][0]['common']
    value7 = data['symptoms'][3]['wound healing'][0]['veg']
    a.append(value1)
    a.append(value2)
    a.append(value3)
    a.append(value4)
    a.append(value5)
    a.append(value6)
    a.append(value7)
    return a

  def reducedappetite():
    a = []
    with open('tensorEnv/sym.json') as f:
      data = json.load(f)
    value1 = data['symptoms'][4]['reduced appetite'][0]['name']
    value2 = data['symptoms'][4]['reduced appetite'][0]['vitamins_and_minerals']
    value3 = data['symptoms'][4]['reduced appetite'][0]['fruits']
    value4 = data['symptoms'][4]['reduced appetite'][0]['non_veg']
    value5 = data['symptoms'][4]['reduced appetite'][0]['others']
    value6 = data['symptoms'][4]['reduced appetite'][0]['common']
    value7 = data['symptoms'][4]['reduced appetite'][0]['veg']
    a.append(value1)
    a.append(value2)
    a.append(value3)
    a.append(value4)
    a.append(value5)
    a.append(value6)
    a.append(value7)
    return a

  def Decrease():
    a = []
    with open('tensorEnv/sym.json') as f:
      data = json.load(f)
    value1 = data['symptoms'][5]['Decrease in concentration level'][0]['name']
    value2 = data['symptoms'][5]['Decrease in concentration level'][0]['vitamins_and_minerals']
    value3 = data['symptoms'][5]['Decrease in concentration level'][0]['fruits']
    value4 = data['symptoms'][5]['Decrease in concentration level'][0]['non_veg']
    value5 = data['symptoms'][5]['Decrease in concentration level'][0]['others']
    value6 = data['symptoms'][5]['Decrease in concentration level'][0]['common']
    value7 = data['symptoms'][5]['Decrease in concentration level'][0]['veg']
    a.append(value1)
    a.append(value2)
    a.append(value3)
    a.append(value4)
    a.append(value5)
    a.append(value6)
    a.append(value7)
    return a



  def bodypain():
    a=[]
    with open('tensorEnv/sym.json') as f:
      data = json.load(f)
    value1 = data['symptoms'][6]['body pain'][0]['name']
    value2 = data['symptoms'][6]['body pain'][0]['vitamins_and_minerals']
    value3 = data['symptoms'][6]['body pain'][0]['fruits']
    value4 = data['symptoms'][6]['body pain'][0]['non_veg']
    value5 = data['symptoms'][6]['body pain'][0]['others']
    value6 = data['symptoms'][6]['body pain'][0]['common']
    value7 = data['symptoms'][6]['body pain'][0]['veg']
    a.append(value1)
    a.append(value2)
    a.append(value3)
    a.append(value4)
    a.append(value5)
    a.append(value6)
    a.append(value7)
    return a


'''
print(value['name'])
print(value['vitamins_and_minerals'])
print(value['fruits'])
print(value['veg'])
print(value['non_veg'])
print(value['others'])
print(value['common'])
k=0
spt = ["feelingweaker", "headache", "lethary", "reduced appetite", "wound healing", "Decrease in concentration level", "body pain" ]

for i in range(6):
    val = spt[k]
    print(val)
    value = data['symptoms'][0][val][0]
    #value1 = value[0]['feelingweaker']
    #value2 = value1[0]['name']
    print(value)
    print(value['name'])
    print(value['vitamins_and_minerals'])
    print(value['fruits'])
    print(value['veg'])
    print(value['non_veg'])
    print(value['others'])
    print(value['common'])
    k=k+1
'''
'''
for state in data['states']:
  del state['area_codes']

with open('new_states.json', 'w') as f:
  json.dump(data, f, indent=2)

spt = ["feelingweaker", "lethary","headache","wound healing" "reduced appetite", "Decrease in concentration level", "body pain" ]
k=0
a=[]


for sym in data['symptoms']:
        print("----------------------------------------------------------------------------------------------------------")

        #print(k)
        key = spt[k]


        value = sym[key]
        print("this is right", value)
        for sy in value:
          print(sy['name'])
          print(sy['vitamins_and_minerals'])
          print(sy['fruits'])
          a.append(sy['fruits'])
          print(sy['veg'])
          print(sy['non_veg'])
          print(sy['others'])
          print(sy['common'])
          k=k+1

print("-----------------------------------------------------------------")
print(a)

'''






'''
class symptom:
    def __init__(self,):
        self.value=value

    def sym(value):

        s=["feeling weaker","headache","lethargy yes/no","reduced appetite","wounds taking a long time to heal","Decrease in concentration level","lack of interest in food","Feeling sleepy","Body pain"]

        result=[]
        for i in range(9):
            print(value[i])
            if value[i] == 1:
                print("yes")
                result.append(s[i])
                print(s[i])
                print("-----------------------------------------------")
            else:
                print("no")
                print("----------------------------------------------------")

        return 0
'''