# print pattern
#         1
#      1    2
#    3    5    8
#  13  21   34  55

def pat(n):
    t=1
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(' ',end="")
        k = k - 1
        for j in range(0, i + 1):
            print(t, end=" ")
        t+=t

        print("")

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
