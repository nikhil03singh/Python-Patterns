# Print Pattern
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
def pat(n):
    for i in range(n):
        for j in range(n):
            print(j+1,end=' ')
        print()

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)

