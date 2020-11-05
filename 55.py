# print pattern
#         1
#       1   2
#     1   2   3
#   1   2   3   4
#     1   2   3
#       1   2
#         1

def pat(n):
    for i in range(n,-(n+1),-1):
        for j in range(1,abs(i)+1):
            print(" ", end=" ")
        t=1
        for j in range(n,abs(i),-1):
            print(" ",t,end=" ")
            t+=1
        print("")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
