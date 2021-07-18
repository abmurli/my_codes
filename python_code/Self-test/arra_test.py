# def solution(A, K):
#     n = len(A)
#     for i in range(n-1):
#         if ((A[i] != A[i+1]) and (A[i] + 1 != A[i+1])):
#             return False
#     if (A[0] != 1 or A[n - 1] != K):
#         return False
#     else:
#         return True
#
#
# A = [1,2,3,3,4,5,6,7]
# K = 7
# func_call = solution(A, K)
# print(func_call)

i = 20
for n in range(1, i+1):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    if n % 3 == 0 and n % 5 != 0:
        print("Fizz")
    if n % 3 != 0 and n % 5 == 0:
        print("Buzz")
    if n % 3 != 0 and n % 5 != 0:
        print(n)

