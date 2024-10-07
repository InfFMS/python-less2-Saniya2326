x = int(input())
if x == 1:
    print (x, 'год')
elif (x%10==2 or x%10 == 3 or x%10 == 4) and x!= 11 and x != 12 and x!= 13 and x!=14 and x!=111 and x!=112 and x!=113 and x!=114:
    print(x, 'года')

elif x == 101:
    print (x, 'год')
else:
    print(x, 'лет')

