def getKthLargest(arr, k):
	#	Write your code here.

	n = len(arr)
	prefix_sum = [0] * (n+1)
	sum_subarray = []

	for i in range(n):
		prefix_sum[i + 1] = prefix_sum[i] + arr[i]

	for i in range(n):
		for j in range(i + 1, n+1):
			sum_subarray.append(prefix_sum[j] - prefix_sum[i])

	
	sum_subarray.sort(reverse=True)

	return sum_subarray[k-1]


# Problem statement
# Given an array of integers, find the Kth largest sum subarray For example, given the array [1, -2, 3, -4, 5] and K = 2, the 2nd largest sum subarray would be [3, -4, 5], which has a sum of 4.

# Please note that a subarray is the sequence of consecutive elements of the array.

# Sample Input 1 :
# 2
# 3 3
# 3 -2 5
# 2 2
# 4 1
# Sample output 1 :
# 3
# 4
# Explanation of Sample output 1 :
# For the first test case, 
# Sum of [0, 0] = 3
# Sum of [0, 1] = 1
# Sum of [0, 2] = 6
# Sum of [1, 1] = -2
# Sum of [1, 2] = 3
# Sum of [2, 2] = 5
# All sum of subarrays are {6, 5, 3, 3, 1, -2} where the third largest element is 3.

# For the second test case, 
# Sum of [0, 0] = 4
# Sum of [0, 1] = 5
# Sum of [1, 1] = 1
# All sum of subarrays are {5, 4, 1} where the second largest element is 4.
# Sample Input 2 :
# 2
# 4 10
# 5 4 -8 6
# 3 1
# 1 2 3
# Sample output 2 :
# -8
# 6
# Explanation of Sample output 2 :
# For the first test case, among the sum of all the subarray, the tenth-largest sum will be -8.

# For the second test case, among the sum of all the subarray, the largest sum will be 6.
