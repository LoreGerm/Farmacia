


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

    def __init__(self,last_id,name,cost,available_date,withdraw_date,description,generic_yn,generic_equivalent_drug_id,other_details):
        self.id = last_id + 1
        self.name = name
        self.cost = cost
        self.available_date = available_date
        self.withdraw_date = withdraw_date
        self.description = description
        self.generic_yn = generic_yn
        self.generic_equivalent_drug_id = generic_equivalent_drug_id
        self.other_details = other_details

    def get_id(self):
        return self.id
    def set_id(self,last_id):
        self.id = last_id + 1

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
        d = [self.get_id(),self.get_name(),self.get_cost(),self.get_available_date(),self.get_withdraw_date(),self.get_description(),self.get_generic_yn(),self.get_generic_equivalent_drug_id(),self.get_other_details()]
        return d




class Drug_company:
    id = 0
    name = ""
    details = ""
    drugs = None   # OBJ Drug_and_Medication

    def __init__(self,last_id,name,details,drugs):
        self.id = last_id + 1
        self.name = name
        self.details = details
        if isinstance(drugs, Drug_and_Medication):
            self.drugs = drugs.model_to_dict()

    def get_id(self):
        return self.id
    def set_id(self,last_id):
        self.id = last_id + 1

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
        if isinstance(drugs, Drug_and_Medication):
            self.drugs = drugs.model_to_dict()

    def model_to_dict(self):
        d = [self.get_id(),self.get_name(),self.get_details(),self.get_drugs()]
        return d