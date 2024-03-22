from typing import List
import heapq

def find_k_smallest_elements(arr: List[int], k: int) -> List[int]:
    heapq.heapify(arr)
    ans = []
    for i in range(k):
        ans.append(heapq.heappop(arr))

    return ans

if __name__ == "__main__":
    a = [2,2,3,5,1,3,6,8]
    print(find_k_smallest_elements(a, 4))