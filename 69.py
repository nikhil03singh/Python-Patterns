# print pattern
#         1
#       2   2
#     3       3
#   4           4
# 5               5
#   4           4
#     3       3
#       2   2
#         1
def pat(n):
    r=1
    t = n // 2 + 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (j == t or j==n-t+1):
                print(r, end=" ")
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
