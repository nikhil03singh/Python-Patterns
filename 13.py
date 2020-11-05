# print pattern
#             A
#           A B A
#         A B C B A
#       A B C D C B A
#     A B C D E D C B A
def pat(n):
    for i in range(1,n):
        for j in range(1,n-i):
            print("  ",end='')
        for j in range(1,i+1):
            print(chr(j+64),end=' ')
        for j in range(i-1,0,-1):
            print(chr(j+64),end=' ')
        print()


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)