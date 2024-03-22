'''
    Time Complexity: O(n)
    Space Complexity: O(n)

    where n is the size of input array
    
'''
from sys import stdin

def printIntersection(arr1, n1, arr2, n2) :
    # write your code here !!!! 
    freq_dict = {}
    intersection = []
    
    # Create a dic to store the frequency of elements in arr1
    for num in arr1:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    for num in arr2:
        if num in freq_dict and freq_dict[num] > 0 :
            # print("ys ", freq_dict[num])
            print(num) 
            freq_dict[num] -= 1


#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

#Main Code   
arr1, n1 = takeInput()
arr2, n2 = takeInput()
printIntersection(arr1, n1, arr2, n2)


# Problem statement
# You have been given two integer arrays/lists (ARR1 and ARR2) of size N and M, respectively. You need to print their intersection; An intersection for this problem can be defined when both the arrays/lists contain a particular value or to put it in other words, when there is a common value that exists in both the arrays/lists.

# Note :
# Input arrays/lists can contain duplicate elements.

# The intersection elements printed would be in the order they appear in the second array/list (ARR2).

# Constraints :
# 0 <= N <= 10^6
# 0 <= M <= 10^6

# Time Limit: 1 sec 
# Sample Input 1 :
# 6
# 2 6 8 5 4 3
# 4
# 2 3 4 7 
# Sample Output 1 :
# 2
# 3 
# 4
# Sample Input 2 :
# 4
# 2 6 1 2
# 5
# 1 2 3 4 2
# Sample Output 2 :
# 1 
# 2 
# 2

