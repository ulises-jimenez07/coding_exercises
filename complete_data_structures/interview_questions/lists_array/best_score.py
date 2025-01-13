'''
Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87
'''

def first_second(my_list):
    max1=max2=0
    for score in my_list:
        if score > max1:
            max2=max1
            max1=score
        elif score> max2:
            max2=score
    return max1,max2
