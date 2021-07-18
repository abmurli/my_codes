# def displaysublist(A):
#     # store all the sublists
#     B = []
#
#     # first loop
#     for i in range(len(A) + 1):
#         print(f"-----{i}-----")
#         for j in range(i + 1, len(A) + 1):
#             print(f"{j}")
#             sub = A[i:j]
#             B.append(sub)
#     return B

subarray = []
def displaysublist(A):
    for i in range(0, len(A)):
        print(f"-----{i}-----")
        for j in range(i+1, len(A) +1):
            print(f"{j}")
            subarray.append(A[i:j])
    return subarray


A = [1, 2, 3, 4]

sublist = displaysublist(A)

print(sublist)
