from sys import *
from collections import *
from math import *
from typing import List
import heapq

class Element:
    def __init__(self, val, idx) -> None:
        self.val = val
        self.idx = idx

    # lt -- less than
    def __lt__(self, obj) -> bool:
        return self.val < obj.val #Gets smallest ele at top Min heap

    def __eq__(self, obj: object) -> bool:
        return self.val == obj.val

def mergeKSortedArrays(kArrays, k:int):
	# Write your code here.
	# kArrays is a list of 'k' lists.
	# Return a list.
    
    ans = []
    ptr = [0 for _ in range(k)]
    heap = [Element(kArrays[i][0], i) for i in range(k)]
    heapq.heapify(heap)

    while len(heap)> 0:
        tp: Element = heapq.heappop(heap)
        ans.append(tp.val)
        ar_idx = tp.idx
    
        if ptr[ar_idx] + 1 < len(kArrays[ar_idx]):
            ptr[ar_idx] += 1
            heapq.heappush(heap, Element(kArrays[ar_idx][ptr[ar_idx]], ar_idx))

    return ans


if __name__ == "__main__":
   print(mergeKSortedArrays([[2,4,5,6], [1,3], [1,2,7]], 3))


	



# Problem statement
# You have been given ‘K’ different arrays/lists, which are sorted individually (in ascending order). You need to merge all the given arrays/list such that the output array/list should be sorted in ascending order.

# Constraints :
# 1 <= T <= 5
# 1 <= K <= 5
# 1 <= N <= 20
# -10^5 <= DATA <= 10^5

# Time Limit: 1 sec 
# Sample Input 1:
# 1
# 2
# 3 
# 3 5 9 
# 4 
# 1 2 3 8   
# Sample Output 1:
# 1 2 3 3 5 8 9 
# Explanation of Sample Input 1:
# After merging the two given arrays/lists [3, 5, 9] and [ 1, 2, 3, 8], the output sorted array will be [1, 2, 3, 3, 5, 8, 9].
# Sample Input 2:
# 1
# 4
# 3
# 1 5 9
# 2
# 45 90
# 5
# 2 6 78 100 234
# 1
# 0
# Sample Output 2:
# 0 1 2 5 6 9 45 78 90 100 234
# Explanation of Sample Input 2 :
# After merging the given arrays/lists [1, 5, 9], [45, 90], [2, 6, 78, 100, 234] and [0], the output sorted array will be [0, 1, 2, 5, 6, 9, 45, 78, 90, 100, 234].