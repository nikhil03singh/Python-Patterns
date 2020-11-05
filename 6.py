# print pattern
#         *
#       *   *
#     *       *
#   *           *
# *               *
#   *           *
#     *       *
#       *   *
#         *
def pat(n):
    for i in range(n):
        for j in range(n):
            if (j + i == n // 2 or i - j == (n // 2) or j - i == (n // 2) or i + j == (n - 1) + (n // 2) ):
                print("*", end=" ")
            else:
                print(" ", end=' ')

        print(" ")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
