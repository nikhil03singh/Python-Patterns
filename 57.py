# print pattern
#           A
#         A   B
#       A   B   C
#     A   B   C   D
#   A   B   C   D   E
#     B   C   D   E
#       C   D   E
#         D   E
#           E

def pat(n):
    for i in range(n,-(n+1),-1):
        for j in range(1,abs(i)+1):
            print(" ", end=" ")
        if (i >= 0):
            t = 1
        else:
            t = j + 1
        for j in range(n,abs(i),-1):
            print(" ",chr(t+64),end=" ")
            t+=1
        print("")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
