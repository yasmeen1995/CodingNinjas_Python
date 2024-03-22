from sys import stdin

def pairSum0(l,n):
    # Write your code here
    freq = {}
    pair_count = 0

    for num in l:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    # Iterate through the array to find pairs summing up to 0
    for num in l:
        complement = -num
        if complement in freq:
            pair_count += freq[complement]

        # If the complement is the same as the current element,
        # decrement the count to exclude the pair (num, num)
        if complement == num:
            pair_count -= 1

    return pair_count // 2 # Since each pair is counted twice, divide the count by 2
                
    
    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))


# Problem statement
# Given a random integer array A of size N. Find and print the count of pair of elements in the array which sum up to 0.

# Note:
# Array A can contain duplicate elements as well.

# Constraints :
# 0 <= N <= 10^4
# Time Limit: 1 sec
# Sample Input 1:
# 5
# 2 1 -2 2 3
# Sample Output 1:
# 2
# Explanation
# (2,-2) , (-2,2) will result in 0 , so the answer for the above problem is 2.