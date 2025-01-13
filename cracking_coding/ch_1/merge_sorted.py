def mergeSortedArrays(array1, array2):
    mergeArray=[]
    arr1_index=0
    arr2_index=0
    l1=len(array1)
    l2=len(array2)
    while (arr1_index< l1 or arr2_index< l2 ):
        if(not arr1_index< l1):
            mergeArray.append(array2[arr2_index])
            arr2_index+=1
        elif(not arr2_index< l2) :
            mergeArray.append(array1[arr1_index])
            arr1_index+=1 
        elif(array1[arr1_index]<array2[arr2_index]):
            mergeArray.append(array1[arr1_index])
            arr1_index+=1
        else:
            mergeArray.append(array2[arr2_index])
            arr2_index+=1
    return mergeArray

print(mergeSortedArrays([0,3,4,31], [3,4,6,30])) 

