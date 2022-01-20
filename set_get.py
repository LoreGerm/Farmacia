from classi.drug import Drug_and_Medication,Drug_company
from classi.fun import *



dm = Drug_and_Medication(0,0,0,0,0,0,0,0,0)
dm1 = Drug_and_Medication(1,0,0,0,0,0,0,0,0)
d = [dm,dm1]

dc = Drug_company(0,0,0,d)

print(dc.model_to_dict())

'''
cont = 0

for attr in p.__dict__:
    print("\t def get_"+attr+"(self):")
    print("\t\treturn self."+attr)
    if attr == "id":
        print("\t def set_id(self,last_id):")
        print("\t\tself.id = last_id + 1")
    else:
        print("\t def set_"+attr+"(self,"+attr+"):")
        print("\t\tself."+attr+" = "+attr)
    print("\n")
    cont += 1

print(cont)

'''
