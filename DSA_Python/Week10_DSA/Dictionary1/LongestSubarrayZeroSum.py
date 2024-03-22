def subsetSum(l):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
   
    prefix_sum = {}  # hashmap
    max_length = 0
    curr_sum = 0

    for i, num in enumerate(l):
        curr_sum += num

        # If the current sum is zero, update the max_length to include the current index
        if curr_sum == 0:
            max_length = i + 1
        
        # Store the current sum and its index in the hashmap
        if curr_sum not in prefix_sum:
            prefix_sum[curr_sum] = i
        else:
            # print('yss ',max_length, i, prefix_sum[curr_sum])
            max_length = max(max_length, i - prefix_sum[curr_sum]) # If the current sum is already in the hashmap, update max_length
        
    return max_length


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))


# Problem statement
# Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.

# Constraints:
# 0 <= N <= 10^8
# Time Limit: 1 sec
# Sample Input 1:
# 10 
#  95 -97 -387 -435 -5 -70 897 127 23 284
# Sample Output 1:
# 5
# Explanation:
# The five elements that form the longest subarray that sum up to zero are: -387, -435, -5, -70, 897 
# Note
# You don't have to print anything. Just complete the definition of the function given and return the value accordingly.