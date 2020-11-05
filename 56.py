# print pattern
#         A
#       B   B
#     C   C   C
#   D   D   D   D
#     C   C   C
#       B   B
#         A
#

def pat(n):
    t=0
    for i in range(n,-(n+1),-1):
        for j in range(1,abs(i)+1):
            print(" ",end=" ")
        for j in range(n,abs(i),-1):
            print(" ",chr(t+64),end=" ")
        if(i>0):
            t+=1
        else:
            t-=1
        print("")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
