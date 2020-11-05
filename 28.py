# print pattern
#       0
#     1 0 1
#   2 1 0 1 2
# 3 2 1 0 1 2 3

def pat(n):
    for i in range(1,n+1):
        for j in range(1,n - i +1):
            print(' ', end=' ')
        for j in range(i, 0, -1):
            print(j-1, end=' ')
        for j in range(2, i + 1):
            print(j-1, end=' ')
        print()


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
