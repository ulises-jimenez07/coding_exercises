#check if two strings are away one edit
def oneEditaway(str1, str2):
    len1=len(str1)
    len2=len(str2)
    if abs(len1-len2) >1:
        return False
    if len1 < len2:
        s1=str1
        s2=str2
    else:
        s1=str2
        s2=str1

    index1=0
    index2=0
    difference=False
    #s1 is the shorter sting
    while ((index1 < len(s1)) and (index2 <len(s2))):
        if s1[index1] != s2[index2]:
            if difference:
                return False
            difference=True
            # if lengths are not the same and the difference was in this char 
            # we must skip increasing the index 1
            if len1 == len2:               
                index1+=1
        else:
            index1+=1
        index2+=1 #always increase index 2
    return True


test_cases = [
# no changes
("pale", "pale", True),
("", "", True),
# one insert
("pale", "ple", True),
("ple", "pale", True),
("pales", "pale", True),
("ples", "pales", True),
("pale", "pkle", True),
("paleabc", "pleabc", True),
("", "d", True),
("d", "de", True),
# one replace
("pale", "bale", True),
("a", "b", True),
("pale", "ble", False),
# multiple replace
("pale", "bake", False),
# insert and replace
("pale", "pse", False),
("pale", "pas", False),
("pas", "pale", False),
("pkle", "pable", False),
("pal", "palks", False),
("palks", "pal", False),
# permutation with insert shouldn't match
("ale", "elas", False),
]



for [text_a, text_b, expected] in test_cases:
     print(oneEditaway(text_a, text_b))



