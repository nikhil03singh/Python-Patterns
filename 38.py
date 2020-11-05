# Print pattern
#       3
#     2 3
#   1 2 3
# 0 1 2 3
#   1 2 3
#     2 3
#       3
def pat(n):
    for i in range(n,-(n+1),-1):
        for j in range(abs(i),0, -1):
            print(" ", end=" ")
        for j in range(abs(i),n):
            print(j, end=" ")
        print(" ")


if __name__ == '__main__':
    n = int(input("Enter number: "))
    pat(n)