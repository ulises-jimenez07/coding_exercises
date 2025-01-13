#comprases a string like aabcccccaaa to a2b1c5a3

def compressed_string(str1):
    #new string
    compressed=[]
    counter=0
    for i in range(len(str1)):
        counter +=1
        #when new char is found or at the end of the str
        # add the char and its counters
        if i+1 >= len(str1) or str1[i] != str1[i+1]:
            compressed.append (str1[i]+str(counter))
            counter=0 
       


    return min(str1, "".join(compressed), key=len)


test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
]

for test in test_cases:
    print(compressed_string(test[0]))