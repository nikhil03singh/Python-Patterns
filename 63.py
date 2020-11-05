# print pattern
#   *           *
#     *       *
#       *   *
#         *
def pat(n):
    t = 1
    y = n * 2 - 1
    for i in range(1, n + 1):
        for j in range(1, n * 2 + 1):
            if (j == t or j == y):
                print("*", end='')
            else:
                print(" ", end="")
        t += 1
        y -= 1
        print()

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
