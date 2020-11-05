# Print pattern
#J
#J S
#J S P
#J S P I
#J S P I D
#J S P I D E
#J S P I D E R
#J S P I D E
#J S P I D
#J S P I
#J S P
#J S
#J
def pat(n,m):
    for i in range(0, n):
        for j in range(0, i):
            print(m[j], end=" ")
        print(" ")
    for i in range(n, -1, -1):
        for j in range(0, i):
            print(m[j], end=" ")
        print(" ")


if __name__ == '__main__':
    m = input("Enter string: ")
    n=len(m)
    pat(n,m)




