# print pattern
#         1
#       1   2
#     1   2   3
#   1   2   3   4
#     2   3   4
#       3   4
#         4

def pat(n):
    t=1
    for i in range(n,-(n+1),-1):
        for j in range(1,abs(i)+1):
            print(" ", end=" ")
        if (i >= 0):
            t = 1
        else:
            t = j + 1
        for j in range(n,abs(i),-1):
            print(" ",t,end=" ")
            t+=1
        print("")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
