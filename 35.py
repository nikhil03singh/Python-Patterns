# Print pattern
# D
# C D
# B C D
# A B C D
# B C D
# C D
# D


def pat(n):
    for i in range(n, -(n + 1), -1):
        for j in range(abs(i),n):
            print(chr(j + 65), end=' ')
        print()


if __name__ == '__main__':
    n = int(input("Enter number: "))
    pat(n)
