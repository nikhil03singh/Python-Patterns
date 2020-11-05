# print pattern
#   *   *   *   *
#     *   *   *
#       *   *
#         *
def pat(n)
    for i in range(n,0,-1):
        for j in range( i, n):
            print("  ", end="")

        for j in range(0,i):
            print(" ","*" , end=" ")
        print("")

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
