from sys import stdin

#Following is the structure of the node class for a Singly Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :
    #Define data members and __init__()
    def __init__(self):
        self.__head = None
        self.__count = 0

    '''----------------- Public Functions of Stack -----------------'''


    def push(self, data) :
        #Implement the push(element) function
        newNode = Node(data)
        newNode.next = self.__head
        
        self.__head = newNode
        self.__count += 1
    
        
    def pop(self) :
        #Implement the pop() function
        if self.isEmpty() is True:
            return -1

        # To return the popped data
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data

    def top(self) :
        #Implement the top() function
        if self.isEmpty() is True:
            return -1
        data = self.__head.data
        return data

    def getSize(self) :
        #Implement the getSize() function
        return self.__count


    def isEmpty(self) :
        #Implement the isEmpty() function
        # if self.__count == 0:
        #     return True
        # else:
        #     return False
        return self.__count == 0



#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2 :
        print(stack.pop())

    elif choice == 3 :
        print(stack.top())

    elif choice == 4 : 
        print(stack.getSize())

    else :
        if stack.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1


# Problem statement
# Implement a Stack Data Structure specifically to store integer data using a Singly Linked List.

# The data members should be private.

# You need to implement the following public functions :

# 1. Constructor:
# It initialises the data members as required.

# 2. push(data) :
# This function should take one argument of type integer. It pushes the element into the stack and returns nothing.

# 3. pop() :
# It pops the element from the top of the stack and in turn, returns the element being popped or deleted. In case the stack is empty, it returns -1.

# 4. top :
# It returns the element being kept at the top of the stack. In case the stack is empty, it returns -1.

# 5. size() :
# It returns the size of the stack at any given instance of time.

# 6. isEmpty() :
# It returns a boolean value indicating whether the stack is empty or not.

# Operations Performed on the Stack:
# Query-1(Denoted by an integer 1): Pushes an integer data to the stack.

# Query-2(Denoted by an integer 2): Pops the data kept at the top of the stack and returns it to the caller.

# Query-3(Denoted by an integer 3): Fetches and returns the data being kept at the top of the stack but doesn't remove it, unlike the pop function.

# Query-4(Denoted by an integer 4): Returns the current size of the stack.

# Query-5(Denoted by an integer 5): Returns a boolean value denoting whether the stack is empty or not.

# Constraints:
# 1 <= q <= 10^5
# 1 <= x <= 5
# -2^31 <= data <= 2^31 - 1 and data != -1

# Where 'q' is the total number of queries being performed on the stack, 'x' is the range for every query and data represents the integer pushed into the stack. 

# Time Limit: 1 second
# Sample Input 1:
# 6
# 1 13
# 1 47
# 4
# 5
# 2
# 3
# Sample Output 1:
# 2
# false
# 47
# 13
# Sample Input 2:
# 4
# 5
# 2
# 1 10
# 5
# Sample Output 2:
# true
# -1
# false
#  Explanation of Sample Input 2:
# There are 4 queries in total.
# The first one is Query-5: It tells whether the stack is empty or not. Since the stack is empty at this point, the output is  'true'.

# The second one is Query-2: It pops the data from the stack. Since at this point in time, no data exist in the stack hence, it prints -1.

# The third one is Query-1: It pushes the specified data 10 into the stack and since the function doesn't return anything, nothing is printed.

# The fourth one is Query-5: It tells whether the stack is empty at this point or not. Since the stack has one element and hence it is not empty, false is printed.