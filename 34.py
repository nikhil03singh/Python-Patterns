# Print pattern
# D
# D C
# D C B
# D C B A
# D C B
# D C
# D


def pat(n):
    for i in range(n - 1, -(n + 1), -1):
        for j in range(n - 1, abs(i) - 1, -1):
            print(chr(j + 65), end=' ')
        print()


if __name__ == '__main__':
    n = int(input("Enter number: "))
    pat(n)
