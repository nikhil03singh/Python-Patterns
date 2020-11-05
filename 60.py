# print pattern
#           5
#         4   4
#       3       3
#     2           2
#   1               1
def pat(n):
    t=n
    for i in range(n):
        for j in range(n*2):
            if (i + j == n or j-i == n):
                print(t, end=" ")
            else:
                print(" ", end=' ')
        t-=1

        print(" ")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
