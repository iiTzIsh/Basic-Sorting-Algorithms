def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key    


arr = [12,6,7,8,10,2,9]



print("Before sorting :")
print(arr)

insertionSort(arr)

print("After sorting :")
print(arr)
