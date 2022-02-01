import json
from time import process_time_ns
from classi.address import Address
from classi.drug import Drug_and_Medication,Drug_company
from classi.fun import *
from classi.people import Physician
from classi.prescription import Prescription
from classi.persistenza import db, persistenza


a = Address("via ciao","5","Atlantide","112233","ATL","oceano","nessuno")

a.save_on_file()

dm = Drug_and_Medication(0,0,0,0,0,0,0,0)
dm1 = Drug_and_Medication(0,0,0,0,0,0,0,0)
d = [dm,dm1]

dc = Drug_company(0,0,d)

print(dc.model_to_dict())





'''
value = db.key_in_tuple(obj) + db.value_in_tuple(obj)
sql = "INSERT INTO address (%s,%s,%s,%s,%s,%s,%s) VALUES (%s,%s,%s,%s,%s,%s,%s)"



value = db.value_in_tuple(a)
ql = "INSERT INTO address (via, number, city, postcode, province, country, other_details) VALUES (%s,%s,%s,%s,%s,%s,%s)"
'''















'''


farmacia = "farmacia.txt"

dm = Drug_and_Medication(0,0,0,0,0,0,0,0,0)
dm1 = Drug_and_Medication(1,0,0,0,0,0,0,0,0)
d = [dm,dm1]

dc = Drug_company(2,0,0,d)
add(dc)
#a = Address(3,0,0,0,0,0,0,0)
#p = Physician(4,a,0,0)
#add(p)

dm2 = Drug_and_Medication(5,0,0,0,0,0,0,0,0)
dc2 = Drug_company(6,0,0,dm2)
add(dc2)

#print(search(dc2))

#reset()



#print(json.loads(stampa(farmacia)))
#print(dm.get_all_item())











if dc2.get_all_item()[1] == dc2.get_all_item()[1]:
    print(True)




print(p.model_to_dict())

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


"drug company id": self.get_id(),
"name": self.get_name(),
"details": self.get_details(),

'''
