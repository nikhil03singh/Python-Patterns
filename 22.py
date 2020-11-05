# Print Pattern
#   * * *
# *   *    *
# * *   * *
# *   *   *
#   * * *

def pat(n):
    for i in range(n):
        for j in range(n):
            if (i + j == n - 1) or(i==j):
                print(" ", end=" ")
            else:
                print("*", end=' ')
        print('')





if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)