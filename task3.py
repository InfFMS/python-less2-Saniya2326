x = int(input())
if x%10 == 1:
    print (x, 'год')
elif x%10 == 2 or x%10 == 3 or x%10 == 4:
    print(x, 'года')
else:
    print(x, 'лет')