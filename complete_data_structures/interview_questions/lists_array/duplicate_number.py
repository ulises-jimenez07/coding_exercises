'''
Duplicate Number
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
'''

def remove_duplicates(arr):
    new_list=[]
    seen=set()
    
    for elem in arr:
        if  elem not in seen:
            new_list.append(elem)
            seen.add(elem)
            
    return new_list