# print pattern
#           A
#         B   B
#       C   C   C
#     D   D   D   D
#   E   E   E   E   E
def pat(n):
    t=65
    for i in range(n):

        for j in range(1, n - i):
            print("  ", end="")

        for j in range(0, i + 1):
            print(" ",chr(t) , end=" ")
        t+=1
        print("")

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
