# print pattern
#  5   4   3   2   1
#    4   3   2   1
#     3   2   1
#        2   1
#          1

def pat(n):
    for i in range(n,0,-1):
        for j in range( i, n):
            print("  ", end="")
        for j in range(i,0,-1):
            print(" ",j , end=" ")
        print("")

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
