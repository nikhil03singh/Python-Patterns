#Print Pattern
#0 0 0 0 0
#1 2 2 2 1
#2 3 3 3 2
#3 4 4 4 3
#4 4 4 4 4

def pat(n):
    for i in range(n):
        for j in range(n):
            if (i==0 or i==n-1 or j==0 or j==n-1):
                print(i, end=" ")
            else:
                print(i+1, end=' ')
        print('')

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)