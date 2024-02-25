
def split_function(input, idx, lsum, rsum):
    size = len(input)
    if idx == size:
        return lsum == rsum
    
    if input[idx] % 5 ==0:
        lsum += input[idx]
    elif input[idx] % 3 == 0:
        rsum += input[idx]
    else:
        return split_function(input, idx+1, lsum+input[idx], rsum) or split_function(input, idx+1, lsum, rsum+input[idx])

    return split_function(input, idx+1, lsum, rsum)


def split_array(input, size):
    return split_function(input, 0, 0, 0)
    
    

def main():
    size = int(input())
    input_array = list(map(int, input().split()))

    if split_array(input_array, size):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()





# Problem statement
# Given an integer array A of size N, check if the input array can be divided in two groups G1 and G2 with following properties-

# - Sum of both group elements are equal
# - Group 1: All elements in the input, which are divisible by 5 
# - Group 2: All elements in the input, which are divisible by 3 (but not divisible by 5). 
# - Elements which are neither divisible by 5 nor by 3, can be put in either group G1 or G2 to satisfy the equal sum property. 
# Group 1 and Group 2 are allowed to be unordered and all the elements in the Array A must belong to only one of the groups.



# Return true, if array can be split according to the above rules, else return false.

# Note: You will get marks only if all the test cases are passed.

# Sample Input 1 :
# 2
# 1 2
# Sample Output 1 :
# false
# Sample Input 2 :
# 3
# 1 4 3
# Sample Output 2 :
# true
  