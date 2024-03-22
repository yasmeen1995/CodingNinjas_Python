
import heapq
from typing import List


class Element:
    def __init__(self, val) -> None:
        self.val = val

       # lt -- less than
    def __lt__(self, obj) -> bool:
        return self.val > obj.val #Gets Largest ele at top Min heap

    def __eq__(self, obj: object) -> bool:
        return self.val == obj.val



def balance(lh: List[Element], uh: List[int]) -> None:
    len_l = len(lh)
    len_r = len(uh)

    if len_l == len_r or len_l == len_r + 1:
        return 
    elif len_l > len_r:
        tp = heapq.heappop(lh)
        heapq.heappush(uh, tp.val)
    else:
        tp = heapq.heappop(uh)
        heapq.heappush(lh, Element(tp))


def findMedian(arr, n):
    # Write your code here
    lh = []
    uh = []
    ans = []

    for i in range(n):
        if len(lh) == 0:
            heapq.heappush(lh, Element(arr[i]))
        else:
            tp: Element = lh[0]
            if arr[i] < tp.val:
                heapq.heappush(lh, Element(arr[i]))
            else:
                heapq.heappush(uh, arr[i])

            balance(lh, uh)

        if i % 2 ==0:
            # Odd ele
            ans.append(lh[0].val)
        else:
            ans.append((lh[0].val + uh[0])//2)

    return ans


if __name__ == "__main__":
    print(findMedian([6,2,1,3,7,5], 6))


# Problem statement
# You are given a stream of 'N' integers. For every 'i-th' integer added to the running list of integers, print the resulting median.

# Print only the integer part of the median.

# Sample Input 1 :
# 6
# 6 2 1 3 7 5
# Sample Output 1 :
# 6 4 2 2 3 4
# Explanation of Sample Output 1 :
# S = {6}, median = 6
# S = {6, 2} -> {2, 6}, median = 4
# S = {6, 2, 1} -> {1, 2, 6}, median = 2
# S = {6, 2, 1, 3} -> {1, 2, 3, 6}, median = 2
# S = {6, 2, 1, 3, 7} -> {1, 2, 3, 6, 7}, median = 3
# S = {6, 2, 1, 3, 7, 5} -> {1, 2, 3, 5, 6, 7}, median = 4
# Sample Input 2 :
# 5
# 5 4 3 2 1
# Sample Output 2 :
# 5 4 4 3 3