A = [11, 15, 22, 33, 22, 44]

for i in range(len(A)):
    for j in range(len(A)-1):
        if A[i] < A[j]:
           A[i], A[j] = A[j], A[i]
        else:
           # print("less", A[i])
            pass
print(A)

# print("max num")
max = A[0]
for i in range(len(A)):
    if A[i] > max:
        max = A[i]
    else:
        pass
print(max)