# print pattern
#           A
#         B   B
#       C       C
#     D           D
#   E               E
def pat(n):
    t = 0
    for i in range(n):

        for j in range(n*2):
            if (i + j == n or j-i == n):
                print(chr(t+65), end=" ")
            else:
                print(" ", end=' ')
        t+=1

        print(" ")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
