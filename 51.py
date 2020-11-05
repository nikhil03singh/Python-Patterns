# print pattern
#   A   B   C   D   E
#     A   B   C   D
#       A   B   C
#         A   B
#           A

def pat(n):
    for i in range(n,0,-1):
        for j in range( i, n):
            print("  ", end="")
        for j in range(0,i):
            print(" ",chr(j+65) , end=" ")
        print("")

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
