#write your code here
class InsufficentFundsException(Exception):
    pass

def withdraw_salary(sal):
    try:
        if sal > 500:
            raise InsufficentFundsException()
    except InsufficentFundsException:
        print("Insufficient funds in the account.")
    else:
        print("Remaining:{}".format(500 - sal))


sal = int(input())
withdraw_salary(sal)


# Problem statement
# Rishabh has recently learnt about custom exceptions. His friend gave him a task to initialise the salary with 500 in a class and raise an exception with message as "Insufficent funds in the account" if the withdrawl amount is greater than the bank balance otherwise display a message as " Remaining:remaining balance"

# Sample Input 1
# 400 
# Sample output 1
#  Remaining:100
# Sample Input 1
# 600
# Sample output 1
# Insufficient funds in the account.
