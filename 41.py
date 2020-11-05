# print pattern
#          * 
#        *   * 
#      *   *   * 
#    *   *   *   * 
#  *   *   *   *   *
def pat(n):
    for i in range(n):

        for j in range(1, n - i):
            print("  ", end="")

        for j in range(0, i + 1):
            print(" ", "*", end=" ")
        print("")

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
