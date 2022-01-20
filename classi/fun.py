import json
import os

farmacia = "farmacia.txt"



# SRIVI NEL FILE
def over_write(file_name,ru):
    f = open(file_name, "w")
    f.write(json.dumps(ru)) 
    f.close()


try:
    size_far = os.path.getsize(farmacia)
    #sizeCess = os.path.getsize(cestino)
except:
    over_write(farmacia,[])
    #Over_write(cestino,[])
    size_far = os.path.getsize(farmacia)
    #sizeCess = os.path.getsize(cestino)





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


# STAMPA IL FILE
def stampa(file):
    f = open(file, "r")
    a = f.read()
    f.close()
    return a


def search():
    pass

'''
def agg_size():
    try:
        size_far = os.path.getsize(farmacia)
        #sizeCess = os.path.getsize(cestino)
    except:
        over_write(farmacia,[])
        #Over_write(cestino,[])
        size_far = os.path.getsize(farmacia)
        #sizeCess = os.path.getsize(cestino)
'''

def add(obj):
    if size_far == 0:
        far = [obj.model_to_dict()]
        over_write(farmacia,far)
        #agg_size()
    else:
        far = json.loads(stampa(farmacia))
        far.append(obj.model_to_dict())
        over_write(farmacia,far)
        #agg_size()
