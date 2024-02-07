'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin

MIN_VALUE = -2147483648

def findLargest(arr, nRows, mCols):
    #Your code goes here
    max_val = MIN_VALUE
    idx = 0
    isRow = True

    #Row wise tranverse
    for i in range(nRows):
        rowsum = 0
        for j in range(mCols): 
            rowsum += arr[i][j]
        
        if rowsum > max_val:
            max_val = rowsum
            idx = i
            isRow = True
    
    #Col wise tranverse
    for i in range(mCols):
        colsum = 0
        for j in range(nRows):
            colsum += arr[j][i]
        
        if colsum > max_val:
            max_val = colsum
            idx = i
            isRow = False
    
    if isRow:
        print('row' + " " + str(idx) + " " + str(max_val))
    else:
        print('column' + " " + str(idx) + " " + str(max_val))



#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1


# Problem statement
# For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest sum(sum of all the elements in a row or column) amongst all the rows/columns.

# Note :
# If there are more than one rows/columns with maximum sum, consider the row/column that comes first. And if ith row and jth column has the same largest sum, consider the ith row as answer.

# Sample Input 1:
# 1
# 3 2
# 6 9 
# 8 5 
# 9 2 
# Sample Output 1:
# column 0 23
