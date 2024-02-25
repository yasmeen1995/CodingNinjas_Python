def binarySearch(a, x, si, ei):
    l = len(a)
    if si > ei:
        return -1
    mid = (si + ei) //2

    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binarySearch(a, x, si, mid - 1)
    else: # a[mid] < x
        return binarySearch(a, x, mid + 1, ei)

binarySearch([1,3,4,5,7,8,9,22,33,45],220, 0, 9 )  

# x == taget to search