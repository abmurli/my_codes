import sys

A = [12, 11, 12, 22, 13]

# Traverse through all array elements
for i in range(len(A)):
    min_index = i
    for j in range(i+1, len(A)):
        if A[min_index] > A[j]:
            min_index = j

    A[i], A[min_index] = A[min_index], A[i]

print(A)