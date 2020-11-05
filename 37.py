# Print pattern
#       3
#     3 2
#   3 2 1
# 3 2 1 0
#   3 2 1
#     3 2
#       3
#
def pat(n):
    for i in range(n,-(n+1),-1):
        for j in range(abs(i),0, -1):
            print(" ", end=" ")
        for j in range(n,abs(i), -1):
            print(j-1, end=" ")
        print(" ")


if __name__ == '__main__':
    n = int(input("Enter number: "))
    pat(n)