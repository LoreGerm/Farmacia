import json
import os



cestino = "classi/file/cestino.json"


# SRIVI NEL FILE
def over_write(file_name,ru):
    f = open(file_name, "w")
    f.write(json.dumps(ru)) 
    f.close()


try:
    size_cess = os.path.getsize(cestino)
except:
    over_write(cestino,[])
    size_cess = os.path.getsize(cestino)


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



# SCORRE LA LISTA DI OBJ E LI TRASFORMA IN DICT
def scorri_lista(list):
    a = []
    for i in list:
        a.append(i.get_id())
    return a


# STAMPA IL FILE
def stampa(file):
    f = open(file, "r")
    a = f.read()
    f.close()
    return a

'''
# CERCA ALL'INTERNO DEL FILE FARMACIA.TXT    AGGIUNGERE RICERCA DIZIONARIO DENTRO DIZIONARIO    (CREARE PIU' FILE PER OGNI OBJ?)
def search(value,indice_dict):
    far = json.loads(stampa(farmacia))
    for i in far:
        if i[indice_dict] == value:
            return True
    return False
'''

# CERCA SE ESISTE (FILE PER OGNI CLASSE?)
def search(obj):
    far = obj.get_all_item()
    for i in far:
        if i == obj.model_to_dict():
            return True
    return False

'''

# ELIMINA L'INTERO FILE FARMACIA.TXT
def reset():
    if size_cess == 0:
        over_write(cestino,json.loads(stampa(farmacia)))
        over_write(farmacia,[])
    else:
        ces = json.loads(stampa(cestino))
        ces.append(json.loads(stampa(farmacia)))
        over_write(cestino,ces)
        over_write(farmacia,[])

'''
############################################ FINIRE
def create(obj):
    for attr in obj.__dict__ - 1:
        x = input("assegna "+attr+": ")

