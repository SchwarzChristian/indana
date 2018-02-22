def deepcopy(value):
    if type(value) is dict:
        return { k: deepcopy(v) for k, v in value.items() }
    if type(value) is list:
        return [ deepcopy(x) for x in value ]
    return value