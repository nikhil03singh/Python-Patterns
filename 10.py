# Print pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
def pat(n):
    for i in range(0, n):
        for j in range(0, i):
            print(j + 1, end=" ")
        print(" ")
    for i in range(n, -1, -1):
        for j in range(0, i):
            print(j + 1, end=" ")
        print(" ")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
