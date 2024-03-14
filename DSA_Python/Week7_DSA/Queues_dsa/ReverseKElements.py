
from sys import stdin
import queue

def reverseKElements(inputQueue, k) :
    #Your code goes here
    if k <= 0 or inputQueue.qsize()==0:
        return inputQueue

    stack = []

    for i in range(k):
        stack.append(inputQueue.get())

    while stack:
        inputQueue.put(stack.pop())

    for _ in range(inputQueue.qsize() - k):
        inputQueue.put(inputQueue.get())

    return inputQueue

'''-------------- Utility Functions --------------'''


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]

def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")


# Problem statement
# For a given queue containing all integer data, reverse the first K elements.

# You have been required to make the desired change in the input queue itself.

# Constraints :
# 1 <= N <= 10^6
# 1 <= K <= N
# -2^31 <= data <= 2^31 - 1

#  Time Limit: 1sec
# Sample Input 1:
# 5 3
# 1 2 3 4 5
# Sample Output 1:
# 3 2 1 4 5
# Sample Input 2:
# 7 7
# 3 4 2 5 6 7 8
# Sample Output 2:
# 8 7 6 5 2 4 3