# print pattern
#           1
#         2   2
#       3   3   3
#     4   4   4   4
#   5   5   5   5   5
#     4   4   4   4
#       3   3   3
#         2   2
#           1

def pat(n):
    t=0
    for i in range(n,-(n+1),-1):
        for j in range(1,abs(i)+1):
            print(" ",end=" ")
        for j in range(n,abs(i),-1):
            print(" ",t,end=" ")
        if(i>0):
            t+=1
        else:
            t-=1
        print("")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
