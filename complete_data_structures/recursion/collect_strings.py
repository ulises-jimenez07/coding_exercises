def collectStrings(obj):
    res = []
    for key in obj:
        if isinstance(obj[key], dict):
            res += collectStrings(obj[key])
        elif isinstance(obj[key], str):
            res.append(obj[key])
    return res


def stringifyNumbers(obj):
    new_obj = obj
    for key in obj:
        if isinstance(obj[key], dict):
            new_obj[key] = stringifyNumbers(obj[key])
        elif isinstance(obj[key], int):
            new_obj[key] = str(obj[key])
    return new_obj
