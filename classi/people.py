from classi.address import Address
from classi.prescription import Credit_card, Prescription
from classi.fun import is_obj,search,scorri_lista
from classi.persistenza import persistence_factory, persistenza

class Physician:
    id = 0
    address = None   # OBJ Address
    prescription = []   # OBJ Prescription
    physician_details = ""
    all_item = []
    file = "classi/file/physician.json"
    p = persistence_factory()

    def __init__(self,address,prescription,physician_details):
        self.physician_details = physician_details
        self.id = id(self)
        if self.get_prescription() == []:
            if isinstance(prescription,list):
                self.prescription = is_obj(prescription,Prescription)
            else:
                self.prescription = [is_obj(prescription,Prescription)]
        else:
            self.prescription.append(is_obj(prescription,Prescription))
        self.address = is_obj(address,Address)
        if self.all_item == []:
            self.all_item.append(self.model_to_dict())
        else:
            assert search(self) == False, f"L'oggetto esiste"
            self.all_item.append(self.model_to_dict())


    def save_on_file(self):
        self.p.get_persistance("file").save(self,self.file)


    def get_all_item(self):
        return self.all_item

    def get_physician_details(self):
        return self.physician_details
    def set_physician_details(self,physician_details):
        self.physician_details = physician_details

    def get_id(self):
        return self.id


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
            "address": self.get_address().get_id(),         
            "prescription": self.get_prescription(),
            "details": scorri_lista(self.get_physician_details())
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
    all_item = []
    file = "classi/file/customer.json"
    p = persistence_factory()

    def __init__(self,address,prescription,credit_card,name,surname,date_became_customer,other_customer_details):
        self.id = id(self)
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
        if self.all_item == []:
            self.all_item.append(self.model_to_dict())
        else:
            assert search(self) == False, f"L'oggetto esiste"
            self.all_item.append(self.model_to_dict())


    def save_on_file(self):
        self.p.get_persistance("file").save(self,self.file)


    def get_all_item(self):
        return self.all_item

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
            "address": self.get_address().get_id(), 
            "prescription": scorri_lista(self.get_prescription()),
            "date became customers": self.get_date_became_customer(),
            "credit card": self.get_credit_card().get_id(),     
            "other details": self.get_other_customer_details()
        }
        return d
    


        
