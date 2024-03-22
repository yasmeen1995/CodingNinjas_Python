
import heapq

def getFourthLargest(arr, n):
    if n < 4:
        return -2147483648
    
    # Create a min heap containing the first 4 elements of the array
    min_heap = arr[:4]
    heapq.heapify(min_heap)
    
    # Iterate through the remaining elements in the array
    for num in arr[4:]:
        # Push the current element onto the heap
        heapq.heappushpop(min_heap, num)
    
    # The top of the min heap will be the fourth largest element
    return min_heap[0]





# Problem statement
# You are given an array consisting of 'N' integers. You have to find the fourth largest element present in the array.

# If there is no such number present in the array, then print the minimum value of an integer which is -2147483648.

# Follow Up:
# Try solving this problem in O(N) time complexity.


# Constraints :
# 1 <= N < 10^6
# -10^6 <= element <= 10^6

# Time Limit: 1 sec
# Sample Input 1:
# 5
# 3 5 1 3 1
# Sample Output 1:
# 1
# Explanation Of Sample Input 1:
# 5 is the largest element, 3 is the second-largest element, again we have a 3 so it's the third largest and 1 is the fourth-largest, hence the answer 1.
# Sample Input 2:
# 4
# 9 9 9 9
# Sample Output 2:
# 9
