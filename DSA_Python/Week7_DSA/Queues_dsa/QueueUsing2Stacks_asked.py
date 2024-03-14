from os import *
from sys import *
from collections import *
from math import *

class Queue:
    # Stacks to be used in the operations.
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    # Enqueues 'X' into the queue. Returns true after enqueuing.
    def enqueue(self, X):
        # Write your code here
        # O(1)
        self.stk1.append(X)
        return True

    """
      Dequeues top element from queue. Returns -1 if the queue is empty, 
      otherwise returns the popped element.
    """
    def dequeue(self):
        # Write your code here
        # O(1)
        if len(self.stk1) == 0 and len(self.stk2) == 0:
            return -1

        if len(self.stk2) == 0:
            while len(self.stk1) != 0:
                element = self.stk1.pop()
                self.stk2.append(element)

        return self.stk2.pop()
            
    def front(self):
        if len(self.stk1) == 0 and len(self.stk2) == 0:
            return -1

        if len(self.stk2) == 0:
            while len(self.stk1) != 0:
                element = self.stk1.pop()
                self.stk2.append(element)

        return self.stk2[-1]

    def size(self):
        return len(self.stk1)

    def isEmpty(self):
        return self.size() == 0


# q = Queue()
# q.enQueue(20)
# q.enQueue(10)
# q.enQueue(2)
# q.enQueue(200)
# print("size:",q.size())
# print("isEmpty:",q.isEmpty())

# while q.isEmpty() is False:
#     print(q.deQueue())
# q.size()
# q.isEmpty()

# Problem statement
# You will be given ‘Q’ queries. You need to implement a queue using two stacks according to those queries. Each query will belong to one of these three types:

# 1 ‘X’: Enqueue element ‘X’  into the end of the nth queue. Returns true after the element is enqueued.

# 2: Dequeue the element at the front of the nth queue. Returns -1 if the queue is empty, otherwise, returns the dequeued element.
# Note:
# Enqueue means adding an element to the end of the queue, while Dequeue means removing the element from the front of the queue.

# Constraints:
# 1 <= Q <= 10^5 
# 1 <= P <= 2
# 1 <= X <= 10^5

# Time limit: 1 sec
# Sample Input 1:
# 7
# 1 2 
# 1 3 
# 2 
# 1 4 
# 1 6 
# 1 7 
# 2
# Sample Output 1:
# True 
# True
# 2
# True
# True
# True
# 3
# Explanation of Sample Output 1:
# For this input, we have the number of queries, 'Q' = 7.

# Operations performed on the queue are as follows:

# push(2): Push element ‘2’ into the queue. This returns true.
# push(3): Push element ‘3’ into the queue. This returns true.
# pop(): Pop the top element from the queue. This returns 2.
# push(4): Push element ‘4’ into the queue. This returns true.
# push(6): Push element ‘6’ into the queue. This returns true.
# push(7): Push element ‘7’ into the queue. This returns true.
# pop(): Pop the top element from the queue. This returns 3.
# Sample Input 2:
# 7
# 1 11 
# 1 51 
# 1 26 
# 2 
# 1 6
# 2
# 2 
# Sample Output 2:
# True
# True
# True
# 11
# True
# 51
# 26
# Explanation for Sample Output 2:
# For this input, we have the number of queries, Q = 7.

# Operations performed on the queue are as follows:

# push(11): Push element ‘11’ into the queue. This returns true.
# push(51): Push element ‘51’ into the queue. This returns true.
# push(26): Push element ‘26’ into the queue. This returns true.
# pop(): Pop the top element from the queue. This returns 11.
# push(6): Push element ‘6’ into the queue. This returns true.
# pop(): Pop the top element from the queue. This returns 51.
# pop(): Pop the top element from the queue. This returns 26.


        
