# print pattern
#       1
#     1 0 1
#   1 0 1 0 1
# 1 0 1 0 1 0 1
#   1 0 1 0 1
#     1 0 1
#       1

def pat(n):
    for i in range(n):

        t = 1
        for j in range(n + i):

            if (j < n - 1 - i):
                print(" ", end=' ')
            else:
                print(t, end=" ")
                if (t == 1):
                    t = 0
                else:
                    t = 1
        print()

    for i in range(0, n):
        t=1
        for j in range(0, i + 1):
            print(" ", end=" ")
        for j in range(0, 2* (n + 1 - i) -5):
            print(t, end=" ")
            if (t == 1):
                t = 0
            else:
                t = 1
        print("")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
