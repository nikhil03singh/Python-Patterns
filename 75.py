# Print Pattern
# 5       5
#   4   4
#     3
#   2   2
# 1       1

def pat(n):
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            if (i + j == n + 1) or(i==j):
                print(i, end=" ")
            else:
                print(" ", end=' ')
        print('')





if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)