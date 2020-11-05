# Print Pattern
# * * * * *
# * * * * *
# * * o * *
# * * * * *
# * * * * *

def pat(n):
    c= (n // 2) + 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i == c and j == c):
                print("o", end=" ")
            else:
                print("*", end=' ')
        print('')


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
