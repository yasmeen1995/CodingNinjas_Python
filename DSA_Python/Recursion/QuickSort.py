
"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""
from typing import List

def quickSort(arr: List[int], startIndex: int, endIndex: int):
    """
    Don't write main().
    Don't read input, it is passed as function argument.
    Change in the given array itself.
    Taking input and printing output is handled automatically.
    """
     # BaseCase:
    if startIndex >= endIndex:
        return -1

    pivot_index  = partition(arr, startIndex, endIndex)   
    quickSort(arr, startIndex, pivot_index - 1)
    quickSort(arr, pivot_index + 1, endIndex)


def partition(a, si, ei):
    pivot = a[si]
    count = 0
    # Find no.of elements smaller than pivot value:
    for i in range(si, ei+1):
        if a[i] < pivot:
            count += 1
    
    # Swapping
    a[si + count], a[si] = a[si], a[si + count]
    pivot_index = si + count

    i = si
    j = ei
    while i < j:
        if a[i] < pivot:
            i += 1
        elif a[j] >= pivot:
            j -= 1
        else:
            # Swap the ele
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    return pivot_index




# Problem statement
# Given the 'start' and the 'end'' positions of the array 'input'. Your task is to sort the elements between 'start' and 'end' using quick sort.

# Note :
# Make changes in the input array itself.

# Sample Input 1 :
# 6 
# 2 6 8 5 4 3
# Sample Output 1 :
# 2 3 4 5 6 8
