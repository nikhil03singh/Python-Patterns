# print pattern
# 5       5
#  4     4
#   3   3
#    2 2
#     1
def pat(n):
    t = 1
    y = n * 2 - 1
    u=n
    for i in range(1,n+1):
        for j in range (1,n*2+1):
            if(j==t or j==y):
                print(u,end='')
            else:
                print(" ",end="")
        t+=1
        y-=1
        u-=1
        print()


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
