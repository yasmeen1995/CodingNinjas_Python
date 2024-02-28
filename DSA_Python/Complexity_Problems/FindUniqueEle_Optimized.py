from sys import stdin

def findUnique(arr, n) :
    #Your code goes here
    a = arr[0]

    for i in range(1, n):
        a = a ^ arr[i]
        # print(a)
        
    return a
       


#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(findUnique(arr, n))

    t-= 1


# Problem statement
# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].

# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.

# You need to find and return that number which is unique in the array/list.

#  Note:
# Unique element is always present in the array/list according to the given condition.

# Sample Input 1:
# 1
# 7
# 2 3 1 6 3 6 2
# Sample Output 1:
# 1
# Sample Input 2:
# 2
# 5
# 2 4 7 2 7
# 9
# 1 3 1 3 6 6 7 10 7
# Sample Output 2:
# 4
# 10