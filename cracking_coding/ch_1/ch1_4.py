# we need to have the same even counts

def is_palindrome_permutation(phrase):
    #dictionary of all charracters
    characters={}
    countodd = 0
    for char in phrase:
        #add each character coung
        if not char.isalpha():
             continue
        if char in characters:
            characters[char]=characters[char]+1
        else: 
            characters[char]=1
            #there should be at most one character with count 1
            #every iteration we count the number of odds
        if characters[char]% 2:
                countodd += 1
        else:
                countodd -= 1
    #return if odds <= 1
    return countodd <= 1
test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]

for test in test_cases:
    print(is_palindrome_permutation(test[0]))
    