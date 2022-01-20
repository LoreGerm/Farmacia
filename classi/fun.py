

def is_obj(obj,type):
    if isinstance(obj, list):
        for i in obj:
            if not isinstance(i, type):
                return []
        return obj
    else:
        if isinstance(obj, type):
            return obj



def scorri_lista(list):
    a = []
    for i in list:
        a.append(i.model_to_dict())    # ERROR
    return a

