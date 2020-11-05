# print pattern
#       A
#     A B C
#   A B C D E
#     A B C
#       A

def pat(n):
    ch = 65
    for i in range(n):

        t = 0
        for j in range(n + i):

            if (j < n - 1 - i):
                print(" ", end=' ')
            else:
                print(chr(ch + t), end=" ")
                t += 1
        print()
    cr=65
    for i in range(0, n):
        t=0
        for j in range(0, i + 1):
            print(" ", end=" ")
        for j in range(0, 2* (n + 1 - i) -5):
            print(chr(cr+t), end=" ")
            t+=1
        print("")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
