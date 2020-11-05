#print Pattern
#                1
#              1   1
#            1   2   1
#          1   3   3   1
#        1   4   6   4   1
def pat(n):
    for i in range(n):
        c = 1
        for j in range(1, n - i):
            print("  ", end="")

        for j in range(0, i + 1):
            print("  ", c, end="")
            c = int(c * (i - j) / (j + 1))
        print()


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)