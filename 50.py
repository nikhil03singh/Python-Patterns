# print pattern
#   E   D   C   B   A
#     D   C   B   A
#       C   B   A
#         B   A
#           A

def pat(n):
    for i in range(n,0,-1):
        for j in range( i, n):
            print("  ", end="")
        for j in range(i,0,-1):
            print(" ",chr(j+64) , end=" ")
        print("")

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
