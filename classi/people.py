from classi.address import Address
from classi.prescription import Credit_card, Prescription
from classi.fun import is_obj


class Physician:
    id = 0
    address = None   # OBJ Address
    prescription = []   # OBJ Prescription
    physician_details = ""

    def __init__(self,last_id,address,prescription,physician_details):
        self.physician_details = physician_details
        self.id = last_id + 1
        if self.get_prescription() == []:
            if isinstance(prescription,list):
                self.prescription = is_obj(prescription,Prescription)
            else:
                self.prescription = [is_obj(prescription,Prescription)]
        else:
            self.prescription.append(is_obj(prescription,Prescription))
        self.address = is_obj(address,Address)

    def get_physician_details(self):
        return self.physician_details
    def set_physician_details(self,physician_details):
        self.physician_details = physician_details

    def get_id(self):
            return self.id
    def set_id(self,last_id):
        self.id = last_id + 1

    def get_address(self):
        return self.address
    def set_address(self,address):
        self.address = is_obj(address,Address)

    def get_prescription(self):
        return self.prescription
    def set_prescription(self,prescription):
        if self.get_prescription() == []:
            if isinstance(prescription,list):
                self.prescription = is_obj(prescription,Prescription)
            else:
                self.prescription = [is_obj(prescription,Prescription)]
        else:
            self.prescription.append(is_obj(prescription,Prescription))

    def model_to_dict(self):
        d = {
            "id": self.get_id(),
            "address": self.get_address().model_to_dict(),         
            "prescription": self.get_prescription(),
            "details": self.get_physician_details()
        }
        return d





class Customer:
    id = 0
    address = None  # OBJ Address
    prescription = []   # OBJ Prescription
    credit_card = None    # OBJ Credit_card
    name = ""
    surname = ""
    date_became_customer = ""
    other_customer_details = ""

    def __init__(self,last_id,address,prescription,credit_card,name,surname,date_became_customer,other_customer_details):
        self.id = last_id + 1
        self.name = name
        self.surname = surname
        self.date_became_customer = date_became_customer
        self.other_customer_details = other_customer_details
        if self.get_prescription() == []:
            if isinstance(prescription,list):
                self.prescription = is_obj(prescription,Prescription)
            else:
                self.prescription = [is_obj(prescription,Prescription)]
        else:
            self.prescription.append(is_obj(prescription,Prescription))
        self.prescription.append(is_obj(prescription,Prescription))
        self.address = is_obj(address,Address) 
        self.credit_card = is_obj(credit_card,Credit_card)

    def get_credit_card(self):
        return self.credit_card_number
    def set_credit_card(self,credit_card): 
        self.credit_card = is_obj(credit_card,Credit_card)

    def get_address(self):
        return self.address
    def set_address(self,address):
        self.address = is_obj(address,Address)

    def get_prescription(self):
        return self.prescription
    def set_prescription(self,prescription):
        if self.get_prescription() == []:
            if isinstance(prescription,list):
                self.prescription = is_obj(prescription,Prescription)
            else:
                self.prescription = [is_obj(prescription,Prescription)]
        else:
            self.prescription.append(is_obj(prescription,Prescription))

    def get_id(self):
        return self.id
    def set_id(self,last_id):
        self.id = last_id + 1

    def get_name(self):
            return self.name
    def set_name(self,name):
        self.name = name

    def get_surname(self):
            return self.surname
    def set_surname(self,surname):
        self.surname = surname

    def get_date_became_customer(self):
            return self.date_became_customer
    def set_date_became_customer(self,date_became_customer):
        self.date_became_customer = date_became_customer

    def get_other_customer_details(self):
            return self.other_customer_details
    def set_other_customer_details(self,other_customer_details):
        self.other_customer_details = other_customer_details

    def model_to_dict(self):
        d = {
            "id": self.get_id(),
            "name": self.get_name(),
            "surname": self.get_surname(),
            "address": self.get_address().model_to_dict(), 
            "prescription": self.get_prescription(),
            "date became customers": self.get_date_became_customer(),
            "credit card": self.get_credit_card().model_to_dict(),     
            "other details": self.get_other_customer_details()
        }
        return d
    


        
