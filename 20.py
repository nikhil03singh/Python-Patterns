# Print Pattern
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1

def pat(n):
    for i in range(n):
        for j in range(n, 0, -1):
            print(j, end=' ')

        print()


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
