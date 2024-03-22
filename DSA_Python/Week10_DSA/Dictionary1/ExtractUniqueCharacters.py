def uniqueChar(s): 
    # Write your code here

    # dic = {}
    # result = ""

    # for ch in s:
    #    if ch not in dic:
    #        result += ch
    #        dic[ch] = True

    result = ""
    for ch in s:
        if ch not in result:
            result += ch 
        
    return result


# Main 
s=input() 
print(uniqueChar(s))


# Problem statement
# Given a string S, you need to remove all the duplicates. That means, the output string should contain each character only once. The respective order of characters should remain same, as in the input string.

# Constraints :
# 0 <= Length of S <= 10^8
# Time Limit: 1 sec
# Sample Input 1 :
# ababacd
# Sample Output 1 :
# abcd
# Sample Input 2 :
# abcde
# Sample Output 2 :
# abcde