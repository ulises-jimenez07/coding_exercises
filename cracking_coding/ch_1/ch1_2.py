def is_permutation(str1, str2):
    # dictionary with string and the times it has been seen
    characters = {}
    if len(str1) != len(str2):
        return False

    # add elements to the dictionary for the first str
    for char in str1:
        if char in characters:
            characters[char] = characters[char] + 1
        else:
            characters[char] = 1
    # for the second string, remove the characters seen
    # if the sum is less than 0 then they do not contain the same characters
    for char in str2:
        if char in characters:
            characters[char] = characters[char] - 1
        else:
            characters[char] = -1
        if characters[char] < 0:
            return False
    return True


is_permutation("dog", "god")
is_permutation("abcd", "bacd")
is_permutation("3563476", "7334566")
is_permutation("wef34f", "wffe34")
is_permutation("dogx", "godz")
is_permutation("2354", "1234")
is_permutation("dcw4f", "dcw5f")
is_permutation("DOG", "dog")
is_permutation("dog ", "dog")
is_permutation("aaab", "bbba")
