
# Python3 program to check
# if a number is Magic
# number.
def isMagic(n):
    count = 0
    sum = 0
    while n > 0:
        count = count + n%10
        print(count)
        sum = 0
        n = int(n/10)

    if count == 10:
        return True



    # sum = 0;
    #
    # # Note that the loop
    # # continues if n is 0
    # # and sum is non-zero.
    # # It stops when n becomes
    # # 0 and sum becomes single
    # # digit.
    # while (n > 0 or sum > 9):
    #     if (n == 0):
    #         n = sum;
    #     sum = 0;
    #     sum = sum + n % 10;
    #     print(sum)
    #     n = int(n / 10);
    #     print(n)
    #
    # # Return true if
    # # sum becomes 1.
    # return True if (sum == 1) else False;

# Driver code
n = 50231
if (isMagic(n)):
    print("magic_number")
else:
    print("no a magic_number")

# This code is contributed
# by mits.