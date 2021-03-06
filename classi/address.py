
from classi.fun import is_obj,scorri_lista,search
from classi.persistenza import persistence_factory, persistenza

class Address:
    id = 0
    via = ""
    number = 0
    city = ""
    postcode = 0
    province = ""
    country = ""
    other_address_details = ""
    all_item = []
    p = persistence_factory()
    db_table = 'address'
    file = "classi/file/address.json"

    def __init__(self,via,number,city,postcode,province,country,other_address_details):
        self.id = id(self) 
        self.via = via
        self.number = number
        self.city = city
        self.postcode = postcode
        self.province = province
        self.country = country
        self.other_address_details = other_address_details
        if self.all_item == []:
            self.all_item.append(self.model_to_dict())
        else:
            assert search(self) == False, f"L'oggetto esiste"
            self.all_item.append(self.model_to_dict())
    
    def save_on_db(self):
        self.p.get_persistance("db").save(self,self.db_table)

    def save_on_file(self):
        self.p.get_persistance("file").save(self,self.file)

    def get_all_item(self):
        return self.all_item

    def get_id(self):
        return self.id

    def get_via(self):
            return self.via     
    def set_via(self,via):      
        self.via = via     

    def get_number(self):       
            return self.number  
    def set_number(self,number):
        self.number = number 

    def get_city(self):
            return self.city    
    def set_city(self,city):    
        self.city = city

    def get_postcode(self):
            return self.postcode
    def set_postcode(self,postcode):
        self.postcode = postcode

    def get_province(self):
            return self.province
    def set_province(self,province):
        self.province = province

    def get_country(self):
            return self.country
    def set_country(self,country):
        self.country = country
        
    def get_other_address_details(self):
            return self.other_address_details
    def set_other_address_details(self,other_address_details):
        self.other_address_details = other_address_details

    def model_to_dict(self):
        d = {
            "id": self.get_id(),
            "via": self.get_via(),
            "number": self.get_number(),
            "city": self.get_city(),
            "postcode": self.get_postcode(),
            "province": self.get_province(),
            "country": self.get_country(),
            "other_details": self.get_other_address_details()
        }
        return d
    


