from typing import List
import heapq

def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    # write your code here
    freq_dict = {}

    for num in arr:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    # Create a min heap to store elements along with their frequencies
    heap = []
    for num, freq in freq_dict.items():
        heapq.heappush(heap, (freq, num))
        # len(heap) > k -- remove the smallest element (with the lowest frequency) from the heap
        # This ensures that the heap always contains the k most frequent elements.
        if len(heap) > k: 
            heapq.heappop(heap)


    # Extract the K most frequent elements from the heap
    result = [elem[1] for elem in heap]

    return result


# Problem statement
# You are given an Integer array ‘ARR’ and an Integer ‘K’.

# Your task is to find the ‘K’ most frequent elements in ‘ARR’. Return the elements in any order.

# For Example:

# You are given ‘ARR’ = {1, 2, 2, 3, 3} and ‘K’ = 2. 

# The answer will {2, 3} as 2 and 3 are the elements occurring most times.


# Sample Input 1:
# 5 2
# 1 2 2 3 3 
# Sample Output 1:
# 2 3
# Explanation of Sample Input 1:
# The answer will {2, 3} as 2 and 3 are the elements occurring the most number of times.
# Sample Input 2:
# 2 2
# 1 2 
# Sample Output 2:
# 1 2
# Constraints:
# 1 <= 'N' <= 10^5
# 1 <= 'K' <= Number of unique elements in ‘ARR’
# 1 <= 'ARR[i]' <= 10^6

# Time Limit: 1 sec