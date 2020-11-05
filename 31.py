# Print pattern
# *
# * *
# * * *
# * *
# *
def pat(n):
    for i in range(0, n):
        for j in range(0, i):
            print("*", end=" ")
        print(" ")
    for i in range(n, -1, -1):
        for j in range(0, i):
            print("*", end=" ")
        print(" ")


if __name__ == '__main__':
    n = int(input("Enter number: "))
    pat(n)
