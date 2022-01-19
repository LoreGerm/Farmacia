from classi.prescription import *



p = Cash(0)


cont = 0

for attr in p.__dict__:
    print("\t def get_"+attr+"(self):")
    print("\t\t return self."+attr)
    if attr == "id":
        print("\t def set_id(self,last_id):")
        print("\t\tself.id = last_id + 1")
    else:
        print("\t def set_"+attr+"(self,"+attr+"):")
        print("\t\tself."+attr+" = "+attr)
    print("\n")
    cont += 1


print(cont)


