# print pattern
# A A A A A
# B B B B
# C C C
# D D
# E
def pat(n):
    num = 65
    for i in range(n):
        ch = chr(num)
        for j in range(n):
            if (i + j <= n-1):
                print(ch, end=" ")
            else:
                print(" ", end=' ')
        num+=1
        print('')
if __name__ =='__main__':
    n = int(input("Enter number : "))
    pat(n)