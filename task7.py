x = int(input())
for j in range (1, x+1):
    if j == 2:
        print(j)
    for i in range(2,j):
        if j%i == 0:
            break
        if i == j-1:
            print(j)