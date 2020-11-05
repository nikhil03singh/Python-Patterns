# Print Pattern
# A       E
#   B   D
#     C
#   B   D
# A       E

def pat(n):
    for i in range(0,n):
        for j in range(0,n):
            if (i + j == n - 1) or(i==j):
                print(chr(j+65), end=" ")
            else:
                print(" ", end=' ')
        print('')


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)