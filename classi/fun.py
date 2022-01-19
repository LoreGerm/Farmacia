

def is_obj(obj,type):
    if isinstance(obj, list):
        for i in obj:
            if not isinstance(i, type):
                return []
        return obj
    else:
        return obj
