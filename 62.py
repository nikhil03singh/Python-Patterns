# print pattern
#           E
#         D   D
#       C       C
#     B           B
#   A               A
def pat(n):
    t=n
    for i in range(n):
        for j in range(n*2):
            if (i + j == n or j-i == n):
                print(chr(t+64), end=" ")
            else:
                print(" ", end=' ')
        t-=1

        print(" ")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
