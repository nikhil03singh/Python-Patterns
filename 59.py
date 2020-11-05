# print pattern
#           1
#         2   2
#       3       3
#     4           4
#   5               5
def pat(n):

    for i in range(n):
        for j in range(n*2):
            if (i + j == n or j-i == n):
                print(i+1, end=" ")
            else:
                print(" ", end=' ')

        print(" ")


if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)
