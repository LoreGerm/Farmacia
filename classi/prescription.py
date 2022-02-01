from multiprocessing.sharedctypes import Value
from classi.drug import Drug_and_Medication
from classi.fun import is_obj, scorri_lista,search
from classi.persistenza import persistence_factory, persistenza


class Prescription():
    _id = 0
    _payment_method = None   # OBJ Ref_Payment_Methods
    _status = None    # OBJ Ref_Prescription_Status
    _item = []     # OBJ Prescription_items
    _issued_date = ""
    _filled_date = ""
    _other_details = ""
    _all_item = []
    file = "classi/file/prescription.json"
    p = persistence_factory()

    def __init__(self,_payment_method,_status,_item,_issued_date,_filled_date,_other_details):
        self._id = id(self)
        self._payment_method = is_obj(_payment_method,Ref_Payment_Methods)
        self._status = is_obj(_status,Ref_Prescription_Status)
        if self.get_item() == []:
            if isinstance(_item,list):
                self._item = is_obj(_item,Prescription_items)
            else:
                self._item = [is_obj(_item,Prescription_items)]
        else:
            self._item.append(is_obj(_item,Prescription_items))
        self._issued_date = _issued_date
        self._filled_date = _filled_date
        self._other_details = _other_details
        if self._all_item == []:
            self._all_item.append(self.model_to_dict())
        else:
            assert search(self) == False, f"L'oggetto esiste"
            self._all_item.append(self.model_to_dict())


    def save_on_file(self):
        self.p.get_persistance("file").save(self,self.file)       

    def get_all_item(self):
        return self._all_item

    def get_payment_method(self):
        return self._payment_method
    def set_payment_method(self,_payment_method):
        self._payment_method = is_obj(_payment_method,Ref_Payment_Methods)
    
    def get_status(self):
        return self._status
    def set_status(self,_status):
        self._status = is_obj(_status,Ref_Prescription_Status)
        
    def get_item(self):
        return self._item
    def set_item(self,_item):
        if self.get_item() == []:
            if isinstance(_item,list):
                self._item = is_obj(_item,Prescription_items)
            else:
                self._item = [is_obj(_item,Prescription_items)]
        else:
            self._item.append(is_obj(_item,Prescription_items))

    def get_id(self):
        return self._id


    def get_issued_date(self):
            return self._issued_date
    def set_issued_date(self,_issued_date):
        self._issued_date = _issued_date

    def get_filled_date(self):
            return self._filled_date
    def set_filled_date(self,_filled_date):
        self._filled_date = _filled_date

    def get_other_details(self):
            return self._other_details
    def set_other_details(self,_other_details):
        self._other_details = _other_details

    def model_to_dict(self):
        d = {
            "_id": self.get_id(), 
            "_item": scorri_lista(self.get_item()),                   
            "_status": self.get_status().get_id(),
            "payment method": self.get_payment_method().get_id(),
            "issued date": self.get_issued_date(),
            "filled date": self.get_filled_date(),
            "other details": self.get_other_details()
        }
        return d
    


class Prescription_items:
    _id = 0
    drug = []    # OBJ Drug_and_Medication
    quantity = 0
    instruction_to_customers = ""
    _all_item = []
    file = "classi/file/prescription_items.json"
    p = persistence_factory()


    def __init__(self,drug,quantity,instruction_to_customers):
        self._id = id(self)
        if self.get_drug() == []:
            if isinstance(drug,Drug_and_Medication):
                self.drug = is_obj(drug,Drug_and_Medication)
            else:
                self.drug = [is_obj(drug,Drug_and_Medication)]
        else:
            self.drug.append(is_obj(drug,Drug_and_Medication))
        self.quantity = quantity
        self.instruction_to_customers = instruction_to_customers
        if self._all_item == []:
            self._all_item.append(self.model_to_dict())
        else:
            assert search(self) == False, f"L'oggetto esiste"
            self._all_item.append(self.model_to_dict())


    def save_on_file(self):
        self.p.get_persistance("file").save(self,self.file)


    def get_all_item(self):
        return self._all_item

    def get_id(self):
        return self._id


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
        if self.get_drug() == []:
            if isinstance(drug,Drug_and_Medication):
                self.drug = is_obj(drug,Drug_and_Medication)
            else:
                self.drug = [is_obj(drug,Drug_and_Medication)]
        else:
            self.drug.append(is_obj(drug,Drug_and_Medication))

    def model_to_dict(self):
        d = {
            "_id": self.get_id(),
            "drug": scorri_lista(self.get_drug()),
            "quantity": self.get_quantity(),
            "indtruction to customers": self.get_instruction_to_customers()
        }
        return d



class Ref_Payment_Methods:
    _id = 0
    descriptio = ""
    _all_item = []
    file = "classi/file/ref_payment_methods.json"
    p = persistence_factory()

    def __init__(self,description):
        self._id = id(self)
        self.descriptio = description
        if self._all_item == []:
            self._all_item.append(self.model_to_dict())
        else:
            assert search(self) == False, f"L'oggetto esiste"
            self._all_item.append(self.model_to_dict())


    def save_on_file(self):
        self.p.get_persistance("file").save(self,self.file)


    def get_all_item(self):
        return self._all_item

    def get_id(self):
        return self._id


    def get_description(self):
        return self.description
    def set_description(self,description):
        self.description = description

    def model_to_dict(self):
        d = {
            "_id": self.get_id(),
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
    _id = 0
    description = ""
    _all_item = []
    file = "classi/file/ref_prescription_status.json"
    p = persistence_factory()

    def __init__(self,description):
        self._id = id(self)
        self.description = description
        if self._all_item == []:
            self._all_item.append(self.model_to_dict())
        else:
            assert search(self) == False, f"L'oggetto esiste"
            self._all_item.append(self.model_to_dict())


    def save_on_file(self):
        self.p.get_persistance("file").save(self,self.file)
        

    def get_all_item(self):
        return self._all_item

    def get_id(self):
        return self._id


    def get_description(self):
        return self.description
    def set_description(self,description):
        self.description = description

    def model_to_dict(self):
        d = {
            "_id": self.get_id(),
            "description": self.get_description()
        }
        return d




