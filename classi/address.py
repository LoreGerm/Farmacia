from classi.people import Customer


class Address:
    id = 0
    via = ""
    number = 0
    city = ""
    postcode = 0
    province = ""
    country = ""
    other_address_details = ""

    def __init__(self,last_id,via,number,city,postcode,province,country,other_address_details):
        self.id = last_id + 1 
        self.via = via
        self.number = number
        self.city = city
        self.postcode = postcode
        self.province = province
        self.country = country
        self.other_address_details = other_address_details     # Opzionale

    def get_id(self):
        return self.id      
    def set_id(self,last_id):   
        self.id = last_id + 1

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

    


