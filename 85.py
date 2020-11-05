# Print Pattern
# o o * o o
# o o * o o
# * * * * *
# o o * o o
# o o * o o

def pat(n):
    for i in range(n):
        for j in range(n):
            if (i ==n//2 or j==n//2):
                print("*", end=" ")
            else:
                print("o", end=' ')
        print('')


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
