# Print pattern
# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11 12 13 14 15
def pat(n,k):

    for i in range(n):
        for j in range(i + 1):

            if (i - j >= 0):
                print(k, end=" ")
            else:
                print(" ", end=' ')
            k = k + 1

        print('')


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n,1)
