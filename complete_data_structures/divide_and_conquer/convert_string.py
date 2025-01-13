def find_min_opearation(s1, s2, index1, index2):
    # need to delete
    if index1 == len(s1):
        return len(s2) - index2
    # need to add
    if index2 == len(s2):
        return len(s1) - index1

    if s1[index1] == s2[index2]:
        return find_min_opearation(s1, s2, index1 + 1, index2 + 1)
    delete_operation = 1 + find_min_opearation(s1, s2, index1, index2 + 1)
    insert_operation = 1 + find_min_opearation(s1, s2, index1 + 1, index2)
    replace_operation = 1 + find_min_opearation(s1, s2, index1 + 1, index2 + 1)
    return min(delete_operation, insert_operation, replace_operation)


print(find_min_opearation("table", "tbrltt", 0, 0))


def findMinOperationBU(s1, s2, tempDict):
    for i1 in range(len(s1) + 1):
        dictKey = str(i1) + "0"
        tempDict[dictKey] = i1
    print(tempDict)
    for i2 in range(len(s2) + 1):
        dictKey = "0" + str(i2)
        tempDict[dictKey] = i2
    print(tempDict)
    for i1 in range(1, len(s1) + 1):
        for i2 in range(1, len(s2) + 1):
            if s1[i1 - 1] == s2[i2 - 1]:
                dictKey = str(i1) + str(i2)
                dictKey1 = str(i1 - 1) + str(i2 - 1)
                tempDict[dictKey] = tempDict[dictKey1]
            else:
                dictKey = str(i1) + str(i2)
                dictKeyD = str(i1 - 1) + str(i2)
                dictKeyI = str(i1) + str(i2 - 1)
                dictKeyR = str(i1 - 1) + str(i2 - 1)
                tempDict[dictKey] = 1 + min(
                    tempDict[dictKeyD], min(tempDict[dictKeyI], tempDict[dictKeyR])
                )
    dictKey = str(len(s1)) + str(len(s2))
    return tempDict[dictKey]


# print(findMinOperationBU("table", "tbrltt", 0, 0))
findMinOperationBU("table", "tbrltt", {})
