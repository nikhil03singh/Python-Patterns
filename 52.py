# print pattern
#          *
#        *   *
#      *   *   *
#    *   *   *   *
#  *   *   *   *   *
#    *   *   *   *
#      *   *   *
#        *   *
#          *

def pat(n):
    for i in range(n,-(n+1),-1):
        for j in range(1,abs(i)+1):
            print(" ",end=" ")
        for j in range(n,abs(i),-1):
            print(" ","*",end=" ")
        print("")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
