#Print pattern
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
def pat(n):
    for i in range(n):
        for j in range(i+1):
            if (i - j >= 0):
                print(j+1, end=" ")
            else:
                print(" ", end=' ')

        print('')
if __name__ =='__main__':
    n = int(input("Enter number : "))
    pat(n)