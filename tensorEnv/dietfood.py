from tensorEnv import sym
import itertools

class dfood:

    def __init__(self,symvalue):
        self.value = symvalue
    

    def redupicate(self,x):
                res = [i for n, i in enumerate(x) if i not in x[:n]]
                return res
    def oneDArray(self,x):
            return list(itertools.chain(*x))
        
    def food(self):
        fe = sym.sympt.feelingweaker()
        print(fe)
        he = sym.sympt.head()
        print(he)
        le = sym.sympt.lethary()
        print(le)
        re = sym.sympt.reducedappetite()
        print(re)
        wo = sym.sympt.woundhealing()
        print(wo)
        de = sym.sympt.Decrease()
        print(de)
        bo = sym.sympt.bodypain()
        print(bo)
        
        print(self.value)

        #name vitmain fruie non other com veg
        vam = []
        fruit = []
        veg = []
        nonv = []
        other = []
        common = []
    

        for j in range(len(self.value)):
            i=self.value[j]

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

        
            
        vam2 = self.oneDArray(vam)
        fruit2= self.oneDArray(fruit)
        veg2= self.oneDArray(veg)
        nonv2= self.oneDArray(nonv)
        other2= self.oneDArray(other)
        common2= self.oneDArray(common)


        print("-----------------------------------------------------removing duplicate ----------------symptoms based----------------------------------------------")


        vam3 = self.redupicate(vam2)
        fruit3 =self.redupicate(fruit2)
        veg3 =self.redupicate(veg2)
        nonv3=self.redupicate(nonv2)
        other3=self.redupicate(other2)
        common3 =self.redupicate(common2)

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
        return vam3,fruit3,veg3,nonv3,common3,other3


