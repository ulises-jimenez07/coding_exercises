def flatten(arr):
    resultArr = []
    for custItem in arr:
        if isinstance(custItem, list):
            resultArr.extend(flatten(custItem))
        else:
            resultArr.append(custItem)
    return resultArr
