# Print pattern
# 2
# 2 1
# 2 1 0
# 2 1
# 2


def pat(n):
    for i in range(0, n):
        t = n
        for j in range(0, i):
            print(t-j-1, end=" ")
        print(" ")
    for i in range(n, -1, -1):
        t = n
        for j in range(0, i):
            print(t-j-1, end=" ")
        print(" ")


if __name__ == '__main__':
    n = int(input("Enter number: "))
    pat(n)
