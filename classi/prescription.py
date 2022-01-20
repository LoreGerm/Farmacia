from multiprocessing.sharedctypes import Value
from classi.drug import Drug_and_Medication
from classi.fun import is_obj


class Prescription():
    id = 0
    payment_method = None   # OBJ Ref_Payment_Methods
    status = None    # OBJ Ref_Prescription_Status
    item = []     # OBJ Prescription_items
    issued_date = ""
    filled_date = ""
    other_details = ""

    def __init__(self,last_id,payment_method,status,item,issued_date,filled_date,other_details):
        self.id = last_id + 1
        self.payment_method = is_obj(payment_method,Ref_Payment_Methods)
        self.status = is_obj(status,Ref_Prescription_Status)
        self.item.append(is_obj(item,Prescription_items))
        self.issued_date = issued_date
        self.filled_date = filled_date
        self.other_details = other_details

    def get_payment_method(self):
        return self.payment_method
    def set_payment_method(self,payment_method):
        self.payment_method = is_obj(payment_method,Ref_Payment_Methods)
    
    def get_status(self):
        return self.status
    def set_status(self,status):
        self.status = is_obj(status,Ref_Prescription_Status)
        
    def get_item(self):
        return self.item
    def set_item(self,item):
        self.item.append(is_obj(item,Prescription_items))

    def get_id(self):
        return self.id
    def set_id(self,last_id):
        self.id = last_id + 1

    def get_issued_date(self):
            return self.issued_date
    def set_issued_date(self,issued_date):
        self.issued_date = issued_date

    def get_filled_date(self):
            return self.filled_date
    def set_filled_date(self,filled_date):
        self.filled_date = filled_date

    def get_other_details(self):
            return self.other_details
    def set_other_details(self,other_details):
        self.other_details = other_details

    def model_to_dict(self):
        d = {
            "prescription id": self.get_id(), 
            "item": self.get_item(),    # CONTROLLA
            "status": self.get_status().model_to_dict(),
            "payment method": self.get_payment_method().model_to_dict(),
            "issued date": self.get_issued_date(),
            "filled date": self.get_filled_date(),
            "other details": self.get_other_details()
        }
        return d
    


class Prescription_items:
    id = 0
    drug = []    # OBJ Drug_and_Medication
    quantity = 0
    instruction_to_customers = ""

    def __init__(self,last_id,drug,quantity,instruction_to_customers):
        self.id = last_id + 1
        self.drug.append(is_obj(drug,Drug_and_Medication))
        self.quantity = quantity
        self.instruction_to_customers = instruction_to_customers

    def get_id(self):
        return self.id
    def set_id(self,last_id):
        self.id = last_id + 1

    def get_quantity(self):
            return self.quantity
    def set_quantity(self,quantity):
        self.quantity = quantity

    def get_instruction_to_customers(self):
            return self.instruction_to_customers
    def set_instruction_to_customers(self,instruction_to_customers):
        self.instruction_to_customers = instruction_to_customers
    
    def get_drug(self):
        return self.drug
    def set_drug(self,drug):
        self.drug.append(is_obj(drug,Drug_and_Medication))

    def model_to_dict(self):
        d = {
            "prescription item id": self.get_id(),
            "drug": self.get_drug(),    # CONTROLLA
            "quantity": self.get_quantity(),
            "indtruction to customers": self.get_instruction_to_customers()
        }
        return d



class Ref_Payment_Methods:
    id = 0
    descriptio = ""
    
    def __init__(self,last_id,description):
        self.id = last_id + 1
        self.descriptio = description

    def get_id(self):
        return self.id
    def set_id(self,last_id):
        self.id = last_id + 1

    def get_description(self):
        return self.description
    def set_description(self,description):
        self.description = description

    def model_to_dict(self):
        d = {
            "payment method id": self.get_id(),
            "description": self.get_description()
        }
        return d



class Cash(Ref_Payment_Methods):
    value = 0
    def __init__(self,value):
        self.value = value

    def get_value(self):
        return self.value
    def set_id(self,value):
        self.value = value

    def model_to_dict(self):
        d = {
            "cash": super().model_to_dict(),
            "value": self.get_value()
        }
        return d




class Credit_card(Ref_Payment_Methods):
    number = 0
    expiry_date = 0

    def __init__(self,number,exipity_date):
        self.number = number
        self.expiry_date = exipity_date

    def get_number(self):
            return self.number
    def set_number(self,number):
        self.number = number

    def get_exipity_date(self):
            return self.exipity_date
    def set_exipity_date(self,exipity_date):
        self.exipity_date = exipity_date
    
    def model_to_dict(self):
        d = {
            "credit card": super().model_to_dict(),
            "number": self.get_number(),
            "exipity date": self.get_exipity_date()
        }
        return d






class Ref_Prescription_Status:
    id = 0
    description = ""
    
    def __init__(self,last_id,description):
        self.id = last_id + 1
        self.description = description

    def get_id(self):
        return self.id
    def set_id(self,last_id):
        self.id = last_id + 1

    def get_description(self):
        return self.description
    def set_description(self,description):
        self.description = description

    def model_to_dict(self):
        d = {
            "prescription status id": self.get_id(),
            "description": self.get_description()
        }
        return d




