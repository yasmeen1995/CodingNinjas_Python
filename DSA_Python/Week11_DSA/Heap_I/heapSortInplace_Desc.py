def heapify(arr, n, pos):
    idx = pos
    while 2 * idx  <= n:
        left = 2 * idx 
        right = 2 * idx + 1
        largest = idx

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest == idx:
            break

        arr[idx], arr[largest] = arr[largest], arr[idx]
        idx = largest


def heapSort(arr):
    ######################
    #PLEASE ADD CODE HERE#
    ######################
    n = len(arr)

    # build Max heap
    for i in range( n//2, -1, -1):
        heapify(arr, n, i)
    
    #  Heap sort
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root (max element) with last element
        heapify(arr, i, 0)  # Heapify the reduced heap



n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr[::-1]:
    print(ele,end=' ')



# Problem statement
# Given an integer array of size N. Sort this array (in decreasing order) using heap sort.

# Note: Space complexity should be O(1).

# Constraints :
# 1 <= n <= 10^6
# Time Limit: 1 sec
# Sample Input 1:
# 6 
# 2 6 8 5 4 3
# Sample Output 1:
# 8 6 5 4 3 2