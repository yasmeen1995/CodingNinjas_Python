def isSortedBetter(a, si):
    l = len(a)

    # si == l-1 ==> completed the list and si == 1 ==> Only one ele left
    if si == l-1 or si == 1:
        return True
    if a[si] > a[si+1]:
        return False
    isSmallerPartSorted = isSortedBetter(a, si+1)
    return isSmallerPartSorted


a = [1,22,3,4,50,6]

print(isSortedBetter(a, 0))
    
