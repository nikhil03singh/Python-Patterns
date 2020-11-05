# Print pattern
#           2
#           1 2
#           0 1 2
#           1 2
#           2


def pat(n):
    for i in range(n,-(n-1),-1):
        for j in range (abs(i),n-1,1):
            print(j,end=' ')
        print()


if __name__ == '__main__':
    n = int(input("Enter number: "))
    pat(n)
