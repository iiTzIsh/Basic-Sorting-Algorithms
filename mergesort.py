# Merge function to combine two sorted subarrays
def merge(A, p, q, r):
    n1 = q - p + 1  # Length of first half
    n2 = r - q  # Length of second half

    # Create temporary arrays L and R
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    # Copy data to temporary arrays L and R
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]

    # Sentinel values to mark the end of the arrays
    L[n1] = float('inf')  # Infinity
    R[n2] = float('inf')  # Infinity

    # Merge the two halves back into A[p..r]
    i = j = 0  # Initial indexes for L and R

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

# Merge sort function to recursively divide the array
def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2  # Middle point
        mergeSort(A, p, q)  # Sort the first half
        mergeSort(A, q + 1, r)  # Sort the second half
        merge(A, p, q, r)  # Merge the sorted halves

# Test the merge sort
A = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", A)

mergeSort(A, 0, len(A) - 1)
print("Sorted array:", A)
