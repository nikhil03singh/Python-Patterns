# print pattern
#           A
#         A   B
#       A   B   C
#     A   B   C   D
#   A   B   C   D   E
def pat(n):
    for i in range(n):
        t=1
        for j in range(1, n - i):
            print("  ", end="")

        for j in range(0, i + 1):
            print(" ",chr(t+64) , end=" ")
            t+=1
        print("")

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
