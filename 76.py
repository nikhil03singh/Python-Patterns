# Print Pattern
# 1       5
#   2   4
#     3
#   2   4
# 1       5

def pat(n):
    for i in range(n):
        for j in range(n):
            if (i + j == n - 1) or(i==j):
                print(j+1, end=" ")
            else:
                print(" ", end=' ')
        print('')





if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)