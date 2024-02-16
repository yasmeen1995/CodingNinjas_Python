def isSorted(a):
    l = len(a)
    # Base case:
    if l == 0 or l == 1:
        return True
    
    if a[0] > a[1]:
        return False
    
    smalletList = a[1:]
    isSmallerListSorted = isSorted(smalletList)

    if isSmallerListSorted:
        return True
    else:
        return False
    
a = [1,2,3,4,7,9,11,0]

print(isSorted(a))