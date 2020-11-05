# print pattern
#         A
#       B   B
#     C       C
#   D           D
# E               E
#   D           D
#     C       C
#       B   B
#         A
def pat(n):
    r=0
    t = n // 2 + 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (j == t or j==n-t+1):
                print(chr(r+65), end=" ")
            else:
                print(" ", end=' ')
        if(i<=n/2):
            t-=1
            r+=1
        else:
            t+=1
            r-=1

        print("")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
