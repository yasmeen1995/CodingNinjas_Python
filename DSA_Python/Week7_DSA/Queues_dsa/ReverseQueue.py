
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

def reverseQueue(inputQueue) :
    # Your code goes here
    if inputQueue.empty():
        return inputQueue

    front_element = inputQueue.get()
    reverseQueue(inputQueue)

    return inputQueue.put(front_element)
    

'''-------------- Utility Functions --------------'''

def takeInput():
    n = int(stdin.readline().strip())

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return qu


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    qu = takeInput()
    reverseQueue(qu)
    
    while not qu.empty() :
        print(qu.get(), end = " ")
        
    print()
    
    t -= 1


# Problem statement
# You have been given a queue that can store integers as the data. You are required to write a function that reverses the populated queue itself without using any other data structures.

# Constraints:
# 1 <= t <= 100
# 1 <= N <= 10^4
# -2^31 <= data <= 2^31 - 1

# Time Limit: 1sec 
# Sample Input 1:
# 1
# 6
# 1 2 3 4 5 10
# Note:
# Here, 1 is at the front and 10 is at the rear of the queue.
# Sample Output 1:
# 10 5 4 3 2 1
# Sample Input 2:
# 2
# 5
# 2 8 15 1 10
# 3
# 10 20 30
# Sample Output 2:
# 10 1 15 8 2 
# 30 20 10 