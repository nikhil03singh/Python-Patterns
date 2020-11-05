# Print pattern
#       D
#     D C
#   D C B
# D C B A
#   D C B
#     D C
#       D
def pat(n):
    for i in range(n,-(n+1),-1):
        for j in range(abs(i),0, -1):
            print(" ", end=" ")
        for j in range(n,abs(i),-1):
            print(chr(j+64), end=" ")
        print(" ")
=

if __name__ == '__main__':
    n = int(input("Enter number: "))
    pat(n)