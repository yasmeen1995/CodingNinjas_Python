from sys import stdin

def tripletSum(arr, n, num) :
	#Your code goes here
    arr.sort()
    ans = 0
    
    for i in range(0, n-3):
        low_j = i + 1
        high = n - 1
        while low_j < high:
            currSum = arr[i] + arr[low_j] + arr[high]
            if currSum == num :
                ans += 1
                tempHigh = high - 1

                while tempHigh > low_j:
                    if arr[high] == arr[tempHigh]:
                        ans += 1
                        tempHigh -= 1
                    else:
                        break

                low_j += 1

            elif currSum > num :
                high -= 1
            else:
                low_j += 1
    return ans



#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(tripletSum(arr, n, num))

    t -= 1


# Problem statement
# You have been given a random integer array/list(ARR) and a number X. Find and return the triplet(s) in the array/list which sum to X.

# Note :
# Given array/list can contain duplicate elements.

# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^3
# 0 <= X <= 10^9

# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 1 2 3 4 5 6 7 
# 12
# Sample Output 1:
# 5
