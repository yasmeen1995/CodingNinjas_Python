from sys import stdin

def findDuplicate(arr, n) :
    #Your code goes here
    arr.sort()

    for i in range(n-1):
            if arr[i] == arr[i+1]:
                return arr[i]



#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip()) 

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1

# Problem statement
# You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). Each number is present at least once. That is, if N = 5, the array/list constitutes values ranging from 0 to 3, and among these, there is a single integer value that is present twice. You need to find and return that duplicate number present in the array.

# # Note :
# Duplicate number is always present in the given array/list.
# Sample Input 1:
# 1
# 9
# 0 7 2 5 4 7 1 3 6
# Sample Output 1:
# 7
# Sample Input 2:
# 2
# 5
# 0 2 1 3 1
# 7
# 0 3 1 5 4 3 2
# Sample Output 2:
# 1
# 3
