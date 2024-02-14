def lastIndexBetter(a,x,si):
    l = len(a)
    if si == l:
        return -1

    smallerListOutput = lastIndexBetter(a, x, si+1)

    if smallerListOutput != -1:
        return smallerListOutput
    else:
        if a[si] == x:
            return si
        else:
            return -1

a = [1,0,2,3,4,5,4,9,6,4,7]

print(lastIndexBetter(a, 4, 0))
