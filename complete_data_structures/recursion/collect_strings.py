def collectStrings(obj):
    res = []
    for key in obj:
        if type(obj[key]) is dict:
            res += collectStrings(obj[key])
        elif type(obj[key]) is str:
            res.append(obj[key])
    return res


def stringifyNumbers(obj):
    new_obj = obj
    for key in obj:
        if type(obj[key]) is dict:
            new_obj[key] = stringifyNumbers(obj[key])
        elif type(obj[key]) is int:
            new_obj[key] = str(obj[key])
    return new_obj
