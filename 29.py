# print pattern
#         1
#       * * *
#     3 3 3 3 3
#   * * * * * * *
# 5 5 5 5 5 5 5 5 5
def pat(n):
    t=1
    u='*'
    w=1
    for i in range(1, n):
        for j in range(1, n - i):
            print("  ", end='')
        if (w%2!=0):
            for j in range(1, i + 1):
                print(t, end=' ')
            for j in range(i - 1, 0, -1):
                print(t, end=' ')
            t+=2
        else:
            for j in range(1, i + 1):
                print(u, end=' ')
            for j in range(i - 1, 0, -1):
                print(u, end=' ')
        w+=1
        print()


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
