# print pattern
# o o o o o
# * o o o o
# * * o o o
# * * * o o
# * * * * o
def pat(n):
    for i in range(n):
        for j in range(n):
            if (i - j > 0):
                print("*", end=" ")
            else:
                print("o", end=' ')
        print('')
if __name__ =='__main__':
    n = int(input("Enter number : "))
    pat(n)