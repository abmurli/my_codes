def ladder(n):
    for x in range(1, n+1):
        print('{}'.format(' ' * (n-x)) + '{}'.format('#' * (x)))


def ladder_1(n):
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i >=j:
                print("#"*j, end= "\n")


def ladder_2(n):
    for i in range(1, n+1):
        print("#"*i, end="\n")

if __name__ == '__main__':
    n = int(input())
    ladder_1(n)
