from classi.fun import is_obj,scorri_lista,search
from classi.persistenza import persistence_factory, persistenza


class Drug_and_Medication:
    id = 0
    name = ""
    cost = 0
    available_date = ""
    withdraw_date = ""
    description = ""
    generic_yn = ""
    generic_equivalent_drug_id = ""
    other_details = ""
    all_item = []
    file = "classi/file/drug_and_medication.json"
    p = persistence_factory()

    def __init__(self,name,cost,available_date,withdraw_date,description,generic_yn,generic_equivalent_drug_id,other_details):
        self.id = id(self)
        self.name = name
        self.cost = cost
        self.available_date = available_date
        self.withdraw_date = withdraw_date
        self.description = description
        self.generic_yn = generic_yn
        self.generic_equivalent_drug_id = generic_equivalent_drug_id
        self.other_details = other_details
        if self.all_item == []:
            self.all_item.append(self.model_to_dict())
        else:
            assert search(self) == False, f"L'oggetto esiste"
            self.all_item.append(self.model_to_dict())


    def save_on_file(self):
        self.p.get_persistance("file").save(self,self.file)
            

    def get_all_item(self):
        return self.all_item

    def get_id(self):
        return self.id

    def get_name(self):
            return self.name
    def set_name(self,name):
        self.name = name

    def get_cost(self):
            return self.cost
    def set_cost(self,cost):
        self.cost = cost

    def get_available_date(self):
            return self.available_date
    def set_available_date(self,available_date):
        self.available_date = available_date

    def get_withdraw_date(self):
            return self.withdraw_date
    def set_withdraw_date(self,withdraw_date):
        self.withdraw_date = withdraw_date

    def get_description(self):
            return self.description
    def set_description(self,description):
        self.description = description

    def get_generic_yn(self):
            return self.generic_yn
    def set_generic_yn(self,generic_yn):
        self.generic_yn = generic_yn

    def get_generic_equivalent_drug_id(self):
            return self.generic_equivalent_drug_id
    def set_generic_equivalent_drug_id(self,generic_equivalent_drug_id):
        self.generic_equivalent_drug_id = generic_equivalent_drug_id

    def get_other_details(self):
            return self.other_details
    def set_other_details(self,other_details):
        self.other_details = other_details

    def model_to_dict(self):
        d = {
            "id": self.get_id(),
            "name": self.get_name(),
            "cost": self.get_cost(),
            "available date": self.get_available_date(),
            "withdraw date": self.get_withdraw_date(),
            "description": self.get_description(),
            "generic yn": self.get_generic_yn(),
            "generic equivalent drug id": self.get_generic_equivalent_drug_id(),
            "other details": self.get_other_details()
        }
        return d



class Drug_company:
    id = 0
    name = ""
    details = ""
    drugs = []  # OBJ Drug_and_Medication
    all_item = []
    file = "classi/file/drug_company.json"
    p = persistence_factory()

    def __init__(self,name,details,drugs):
        self.id = id(self)
        self.name = name
        self.details = details
        if self.get_drugs() == []:
            if isinstance(drugs,list):
                self.drugs = is_obj(drugs,Drug_and_Medication)
            else:
                self.drugs = [is_obj(drugs,Drug_and_Medication)]
        else:
            self.drugs.append(is_obj(drugs,Drug_and_Medication))
            if self.all_item == []:
                self.all_item.append(self.model_to_dict())
            else:
                assert search(self) == False, f"L'oggetto esiste"
                self.all_item.append(self.model_to_dict())

    
    def save_on_file(self):
        self.p.get_persistance("file").save(self,self.file)
    

    def get_all_item(self):
        return self.all_item

    def get_id(self):
        return self.id

    def get_name(self):
            return self.name
    def set_name(self,name):
        self.name = name

    def get_details(self):
            return self.details
    def set_details(self,details):
        self.details = details

    def get_drugs(self):
        return self.drugs
    def set_drugs(self,drugs):
        if self.get_drugs() == []:
            if isinstance(drugs,list):
                self.drugs = is_obj(drugs,Drug_and_Medication)
            else:
                self.drugs = [is_obj(drugs,Drug_and_Medication)]
        else:
            self.drugs.append(is_obj(drugs,Drug_and_Medication))

    def model_to_dict(self):
        d = {
            "id": self.get_id(),
            "name": self.get_name(),
            "details": self.get_details(),
            "drug": scorri_lista(self.get_drugs())
        }
        return d