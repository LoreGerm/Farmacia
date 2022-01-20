import json



# CONTROLLA SE OBJ è UN OGGETTO
def is_obj(obj,type):
    if isinstance(obj, list):
        for i in obj:
            if not isinstance(i, type):
                return []
        return obj
    else:
        if isinstance(obj, type):
            return obj



# SCORRE LA LISTA DO OBJ E LI TRASFORMA IN DICT
def scorri_lista(list):
    a = []
    for i in list:
        a.append(i.model_to_dict())
    return a



# SRIVI NEL FILE
def over_write(file_name,ru):
    f = open(file_name, "w")
    f.write(json.dumps(ru)) 
    f.close()


# STAMPA IL FILE
def stampa(file):
    f = open(file, "r")
    a = f.read()
    f.close()
    return a
