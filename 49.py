# print pattern
#   E   E   E   E   E
#     D   D   D   D
#       C   C   C
#         B   B
#           A

def pat(n):
    t=65+n-1
    for i in range(n,0,-1):
        for j in range( i, n):
            print("  ", end="")
        for j in range(i,0,-1):
            print(" ",chr(t) , end=" ")
        t-=1
        print("")

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
