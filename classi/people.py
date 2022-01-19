from classi.address import Address
from classi.prescription import Credit_card, Prescription


class Physician:
    id = 0
    address = None   # OBJ Address
    prescription = None   # OBJ Prescription
    physician_details = ""

    def __init__(self,address,physician_details,last_id,prescription):
        self.physician_details = physician_details
        self.id = last_id + 1 
        if isinstance(prescription, Prescription):
            self.prescription = prescription.model_to_dict()
        if isinstance(address, Address):
            self.address = address.model_to_dict()

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
        if isinstance(address, Address):
            self.address = address.model_to_dict()

    def get_prescription(self):
        return self.prescription
    def set_prescription(self,prescription):
        if isinstance(prescription, Prescription):
            self.prescription = prescription.model_to_dict()

    def model_to_dict(self):
        d = [self.get_id(),self.get_address(),self.get_prescription(),self.get_physician_details()]
        return d





class Customer:
    id = 0
    address = None  # OBJ Address
    prescription = None   # OBJ Prescription
    credit_card = None    # OBJ Credit_card
    name = ""
    surname = ""
    date_became_customer = ""
    other_customer_details = ""

    def __init__(self,credit_card,prescription,last_id,name,date_became_customer,other_customer_details,address,surname):
        self.id = last_id + 1
        self.name = name
        self.surname = surname
        self.date_became_customer = date_became_customer
        self.other_customer_details = other_customer_details  # Opzionale
        if isinstance(address, Address):
            self.address = address.model_to_dict()
        if isinstance(prescription, Prescription):
            self.prescription = prescription.model_to_dict()
        if isinstance(credit_card, Credit_card):
            self.credit_card = credit_card.model_to_dict()

    def get_credit_card(self):
        return self.credit_card_number
    def set_credit_card(self,credit_card):
        if isinstance(credit_card, Credit_card):
            self.credit_card = credit_card.model_to_dict()

    def get_address(self):
        return self.address
    def set_address(self,address):
        if isinstance(address, Address):
            self.address = address.model_to_dict()

    def get_prescription(self):
        return self.prescription
    def set_prescription(self,prescription):
        if isinstance(prescription, Prescription):
            self.prescription = prescription.model_to_dict()

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
        d = [self.get_id(),self.get_name(),self.get_surname(),self.get_address(),self.get_prescription(),self.get_date_became_customer(),self.get_credit_card_number(),self.get_other_customer_details()]
        return d
    


        
