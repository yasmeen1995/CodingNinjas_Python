from sys import stdin

def pairSum(arr, n, num) :
	#Your code goes here
    pair_count = 0
    freq_dict = {}

    for element in arr:
        diff = num - element
        # print('ys ', diff)

        if diff in freq_dict:
            pair_count += freq_dict[diff]

        freq_dict[element] = freq_dict.get(element, 0) + 1

    return pair_count

# def pairSum(arr, n, num):
#     arr.sort()
    
#     endIndex = len(arr) - 1
#     startIndex = 0
#     num_pair = 0
    
#     while startIndex < endIndex:
#         if arr[startIndex] + arr[endIndex] < num:
#             startIndex += 1
#         elif arr[startIndex] + arr[endIndex] > num:
#             endIndex -= 1
#         else:
#             element_at_start = arr[startIndex]
#             element_at_end = arr[endIndex]
            
#             if element_at_start == element_at_end:
#                 total_element_from_start_to_end = endIndex - startIndex - 1
#                 num_pair += total_element_from_start_to_end * (total_element_from_start_to_end - 1) // 2
#                 return num_pair
            
#             temp_start_index = startIndex + 1
#             temp_end_index = endIndex - 1
            
#             while temp_start_index <= temp_end_index and arr[temp_start_index] == element_at_start:
#                 temp_start_index += 1
            
#             while temp_end_index >= temp_start_index and arr[temp_end_index] == element_at_end:
#                 temp_end_index -= 1
            
#             total_element_from_start = temp_start_index - startIndex
#             total_element_from_end = endIndex - temp_end_index
            
#             num_pair += total_element_from_start * total_element_from_end
            
#             startIndex = temp_start_index
#             endIndex = temp_end_index
    
#     return num_pair




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
    print(pairSum(arr, n, num))

    t -= 1


# Problem statement
# You have been given an integer array/list(ARR) and a number 'num'. Find and return the total number of pairs in the array/list which sum to 'num'.

# Note:
# Given array/list can contain duplicate elements. 

# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^4
# 0 <= num <= 10^9

# Time Limit: 1 sec

# Sample Input 1:
# 1
# 9
# 1 3 6 2 5 4 3 2 4
# 7
# Sample Output 1:
# 7
