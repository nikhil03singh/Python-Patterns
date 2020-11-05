# Print pattern
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *
def pat(n):
    for i in range(n,-(n+1),-1):
        for j in range(abs(i),0, -1):
            print(" ", end=" ")
        for j in range(abs(i), n):
            print("*", end=" ")
        print(" ")


if __name__ == '__main__':
    n = int(input("Enter number: "))
    pat(n)