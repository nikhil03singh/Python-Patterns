# print pattern
#       A
#     A B A
#   A B C B A
#     A B A
#       A
def pat(n):
    for i in range(1, n + 1):
        for j in range(1, (n + 1) - i):
            print("  ", end='')
        for j in range(1, i + 1):
            print(chr(j + 64), end=' ')
        for j in range(i - 1, 0, -1):
            print(chr(j + 64), end=' ')
        print()
    for i in range(0, n):
        for j in range(0, i + 1):
            print(" ", end=" ")
        for j in range(0,(n + 1 - i)-2):
            print(chr(j+65), end=" ")
        for j in range((n + 1 - i)-3,0,-1):
            print(chr(j+64), end=" ")
        print("")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
