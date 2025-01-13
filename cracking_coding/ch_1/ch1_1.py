#Check if a string only have unique elements
def is_unique(str):
    #create a set (similar to hash table)
    characters=set()
    for char in str:
        #if the character has been seen before, then duplicate
        if char in characters:
            return False
        characters.add(char)
    return True

test_cases = [
    ("abcd", True),
    ("s4fad", True),
    ("", True),
    ("23ds2", False),
    ("hb 627jh=j ()", False),
    ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
    ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
]

print(is_unique("23ds2"))