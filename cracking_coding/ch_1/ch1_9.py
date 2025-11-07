# write a code to check is s2 is a rotation of s1


def isStringRotation(s1, s2):
    if len(s1) == len(s2):
        return s1 in s2 * 2
    return False


test_cases = [
    ("waterbottle", "erbottlewat", True),
    ("foo", "bar", False),
    ("foo", "foofoo", False),
]

for test in test_cases:
    print(isStringRotation(test[0], test[1]))
