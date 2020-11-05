# Print Pattern
# 5       1 
#   4   2   
#     3     
#   4   2   
# 5       1 

def pat(n):
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            if (i + j == n + 1) or(i==j):
                print(j, end=" ")
            else:
                print(" ", end=' ')
        print('')





if __name__ == '__main__':
    n = int(input("Enter number : "))
    pat(n)