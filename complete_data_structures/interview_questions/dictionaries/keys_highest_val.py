'''
Key with the Highest Value
Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))
Output:

b
'''


import sys
def max_value_key(my_dict):
    # TODO
    max_val= -sys.maxsize-1
    max_key=""
    for key, value in my_dict.items():
        if value> max_val:
            max_key=key
            max_val=value
    return max_key