def isPalindrome(string: str) -> bool:
    l = len(string)
    if l == 0 or l == 1:
        return True
    
    if string[0] != string[l-1]:
        return False

    smallAns = isPalindrome(string[1:-1])

    return smallAns
    


# Problem statement
# Determine if a given string ‘S’ is a palindrome using recursion. Return a Boolean value of true if it is a palindrome and false if it is not.

# Note: You are not required to print anything, just implement the function. Example:
# Input: s = "racecar"
# Output: true
# Explanation: "racecar" is a palindrome.

# Sample Input 1:
# abbba
# Sample Output 1:
# true
