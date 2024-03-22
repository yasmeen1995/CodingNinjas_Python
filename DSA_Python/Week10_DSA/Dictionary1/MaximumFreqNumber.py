# Read input as sepcified in the question
# Print output as specified in the question
from sys import stdin

def findMaxFrequency(list):
    freq = {}
    for num in list:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1   
        
    max_val = 0
    max_key = list[0]
    for key in freq.keys():
        if freq[key] > max_val:
            max_val = freq[key]
            max_key = key
    
    return max_key

n=int(input())
list=list(int(i) for i in input().strip().split(' '))
print(findMaxFrequency(list))


# # Taking input
# def takeInput():
#     n = int(input().strip())
#     arr = list(map(int, input().strip().split()))
#     return arr, n


# t = int(input().strip())

# while t > 0:
#     arr, n = takeInput()
#     print(findMaxFrequency(arr))
#     t -= 1


# Problem statement
# You are given an array of integers that contain numbers in random order. Write a program to find and return the number which occurs the maximum times in the given input.

# If two or more elements are having the maximum frequency, return the element which occurs in the array first.

# Constraints:
# 0 <= N <= 10^8
# Time Limit: 1 sec
# Sample Input 1 :
# 13
# 2 12 2 11 12 2 1 2 2 11 12 2 6 
# Sample Output 1 :
# 2
# Sample Input 2 :
# 6
# 7 2 2 4 8 4
# Sample Output 2 :
# 2
# Explanation:
# Here, both element '2' and element '4' have same frequency but '2' ocurr first in orignal array that's why we are returning '2' as output.

