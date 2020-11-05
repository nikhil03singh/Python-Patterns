# print pattern
#   5   5   5   5   5
#     4   4   4   4
#       3   3   3
#         2   2
#           1
def pat(n):
    t=n
    for i in range(n,0,-1):
        for j in range( i, n):
            print("  ", end="")

        for j in range(0,i):
            print(" ",t , end=" ")
        t-=1
        print("")

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
