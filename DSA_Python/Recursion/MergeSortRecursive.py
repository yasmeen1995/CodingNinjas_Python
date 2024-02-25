def mergeSort(arr: [int], l: int, r: int):
    if l == r:
        return
    
    mid = (l + r) // 2

    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)

    merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    len1 = mid - l + 1
    len2 = r - mid
    leftArr = [0] * len1
    rightArr = [0] * len2

    for i in range(len1):
        leftArr[i] = arr[l + i]
    
    for j in range(len2):
        rightArr[j] = arr[mid + 1 + j]

    ptrA, ptrB, ptrC = 0, 0, l

    while ptrA < len1 and ptrB < len2:
        if leftArr[ptrA] < rightArr[ptrB]:
            arr[ptrC] = leftArr[ptrA]
            ptrA += 1
        else:
            arr[ptrC] = rightArr[ptrB]
            ptrB += 1
        ptrC += 1

    while ptrA < len1:
        arr[ptrC] = leftArr[ptrA]
        ptrA += 1
        ptrC += 1

    while ptrB < len2:
        arr[ptrC] = rightArr[ptrB]
        ptrB += 1
        ptrC += 1

# Print statements for debugging

N = int(input())
arr = list(map(int, input().split(' ')))
l, r = 0, N - 1
mergeSort(arr, l, r)

print(*arr)

