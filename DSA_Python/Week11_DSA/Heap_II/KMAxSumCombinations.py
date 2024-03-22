import heapq

from typing import List

class Element:
    def __init__(self, val, id1, id2) -> None:
        self.val = val
        self.id1 = id1
        self.id2 = id2

    def __lt__(self, o) -> bool:
        return self.val > o.val

    def __eq__(self, __o: object) -> bool:
        return self.val == __o.val


def kMaxSumCombination(a: List[int], b: List[int], n: int, k: int) -> List[int]:
    # write your code here
    a.sort(reverse=True)
    b.sort(reverse=True)

    ans = []
    heap = [Element(a[0]+ b[0], 0, 0)]
    taken = {}
    taken[(0,0)] = True

    for _ in range(k):
        tp: Element = heapq.heappop(heap)
        ans.append(tp.val)
        id1, id2 = tp.id1, tp.id2

        if (id1 + 1) < n and not taken.get((id1+1, id2), False):
            heapq.heappush(heap, Element(a[id1+1]+b[id2], id1+1, id2))
            taken[(id1+1, id2)] = True

        if (id2 + 1) < n and not taken.get((id1, id2+1), False):
            heapq.heappush(heap, Element(a[id1]+b[id2+1], id1, id2+1))
            taken[(id1, id2+1)] = True

    return ans


if __name__ == "__main__":
    a = [1,3,5]
    b = [6,4,2]

    print(kMaxSumCombination(a,b,3,2))
    






# Problem statement
# You are given two arrays/lists ‘A’ and ‘B’ of size ‘N’ each. You are also given an integer ‘K’.

# You must return ‘K’ distinct maximum and valid sum combinations from all the possible sum combinations of the arrays/lists ‘A’ and ‘B’.

# Sum combination adds one element from array ‘A’ and another from array ‘B’.

# For example :
# A : [1, 3] 
# B : [4, 2] 
# K: 2

# The possible sum combinations can be 5(3 + 2), 7(3 + 4), 3(1 + 2), 5(1 + 4). 

# The 2 maximum sum combinations are 7 and 5. 

# Sample Input 1 :
# 3 2
# 1 3 5
# 6 4 2
# Sample Output 1 :
# 11 9
# Explanation of Sample Output 1 :
# For the given arrays/lists, all the possible sum combinations are: 
# 7(1 + 6), 5(1 + 4), 3(1 + 2), 9(3 + 6), 7(3 + 4), 5(3 + 2), 11(6 + 5), 9(5 + 4), 7(5 + 2).

# The two maximum sum combinations from the above combinations are 11 and 9. 
# Sample Input 2 :
# 2 1
# 1 1
# 1 1
# Sample Output 2 :
# 2
# Explanation of sample input 2 :
# For the given arrays/lists, two possible sum combinations are 2(1 + 1), and 2(1 + 1).
# Constraints :
# 1 <= N <= 100
# 1 <= K <= N
# -10^5 <= A[i], B[i] <= 10^5

# 'A[i]' and 'B[i]' denote the ith element in the given arrays/lists. 

# Time limit: 1 sec


