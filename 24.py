# print pattern
#     1
#    0 1
#   0 1 0
#  1 0 1 0
# 1 0 1 0 1
def pat(n):
    t=1
    for i in range(n):

        for j in range(1, n - i):
            print("  ", end="")

        for j in range(0, i + 1):
            print("  ", t, end="")
            if(t==1):
                t=0
            else:
                t=1
        print("")

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
