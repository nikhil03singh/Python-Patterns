# print pattern
# *
# * *
# * * *
# * * * *
# * * * * *
def pat(n):
    for i in range(n):
        for j in range(i+1):
            if (i - j >= 0):
                print("*", end=" ")
            else:
                print(" ", end='')
        print('')
if __name__ =='__main__':
    n = int(input("Enter number : "))
    pat(n)