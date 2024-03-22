from os import *
from sys import *
from collections import *
from math import *

def kMinFloor(squareCity, n, k):
	# Write your code here.
	flattened = []
	for row in squareCity:
		flattened.extend(row)

	flattened.sort()

	return flattened[k-1]



# Problem statement
# Ninja is appointed as an architect in Square City. As the name suggests, all the ‘N’ * ‘N’ buildings in the Square City are constructed in a square grid with ‘N’ rows and ‘N’ columns. Each building has a fixed number of floors and is arranged in a row and column in non decreasing order of the number of floors.

# For example: One of the Square City with ‘N = 3’ is shown below:

# alt

# Ninja wants to develop the Square City. So, he selects the ‘K’the building with minimum floors and plans to work on it. As he is busy deciding the design and infrastructure for that building, he asks you for help.

# For Example: For the given Square City and ‘K’ = 4, the 4th building having the minimum number of floors is at (2,0) and having 11 floors.

# text

# Can you help Ninja find the building with ‘K’the building with minimum floors?

# Sample Input 1 :
# 2
# 3 4
# 1 2 8
# 4 10 11
# 6 11 12
# 1 1
# 4    
# Sample Output 1 :
# 6
# 4
# Explanation for Sample Input 1 :
# For the first test case, if we write all the floors in increasing order then the 4th building from the beginning will be 6 as shown below:
# 1, 2, 4, 6, 8, 10, 11, 11, 12

# For the second test case, we have only one building in the smart city so this will be the 1’st minimum.
# Sample Input 2 :
# 1
# 2 4
# 1 9
# 14 16
# Sample Output 2 :
# 16
# Explanation for Sample Input 2 :
# If we write all the floors in increasing order then the 4’th minimum will be 16 as shown below:
# 1 9 14 16