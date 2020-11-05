# Print Pattern
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
def pat(n):
    for i in range(n):
        for j in range(n):
            print(i+1,end=' ')
        print()

if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)