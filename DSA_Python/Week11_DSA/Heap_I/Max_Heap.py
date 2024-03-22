class Heap:
    def __init__(self, max_size: int) -> None:
        self.heap = [0 for _ in range(max_size)]
        self.size = 0
    """
    a is current, b is target
    Return true if b is to swapped with a
    """
    def compare(self, a, b) -> bool:
        return b > a
    
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    # Insert val into the heap
    def insert(self, val:int) -> None:
        self.size += 1
        # Inserted val at end of heap
        self.heap[self.size] = val

        # Move the value to its actual place according to max or min
        idx = self.size

        while idx > 1:
            parent = idx // 2
            if self.compare(self.heap[parent], self.heap[idx]):
                self.swap(parent, idx)
                idx = parent
            else:
                break

    def heapify(self, pos) -> None:
        idx = pos
        # Going till it is not a leave node
        while 2 * idx <= self.size:
            g = idx
            left = 2 * idx
            right = 2 * idx + 1
            # Comparing root with left 
            if self.compare(self.heap[idx], self.heap[left]):
                g = left

            # Comparing left with right 
            if right <= self.size and self.compare(self.heap[g], self.heap[right]):
                g = right
            
            # Current node is at actual position (nop swap required)
            if g == idx:
                break

            self.swap(g, idx)
            idx = g

    def remove(self) -> int:
        self.swap(1, self.size)
        self.size -= 1
        self.heapify(1)

        return self.heap[self.size + 1]


    def print(self) -> None:
        print("Heap is: ")
        for i in range(1, self.size+1):
            print(self.heap[i],)
        print("\n==============")


if __name__ == "__main__":
    heap = Heap(10)
    heap.insert(10)
    heap.insert(20)
    heap.insert(30)
    heap.insert(25)
    heap.insert(35)

    heap.print()
