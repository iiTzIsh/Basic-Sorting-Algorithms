
def partition(arr,lb,ub):
    i=(lb-1)                   #index of the smaller element
    pivot = arr[ub]            #pivot

    for j in range(lb,ub):
                               #if current element is smaller than or equal to pivote
        if arr[j] <= pivot:
                               #increment the index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            
    arr[i+1],arr[ub] = arr[ub],arr[i+1]
    
    return (i+1)





def quickSort(arr,lb,ub):
    if lb<ub:
                                        #partition index - pi
        pi = partition(arr,lb,ub)
        
                                        #seperately sort the elements in before partition and after partition
        quickSort(arr,lb,pi-1)
        quickSort(arr,pi+1,ub)



arr = [12,6,7,8,10,2,9]







print("Before sorting :")
print(arr)

lb=0
ub = len(arr)-1

quickSort(arr,lb,ub)

print("After sorting :")
print(arr)
