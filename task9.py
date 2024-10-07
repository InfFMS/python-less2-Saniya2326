x = int (input())
y = int(input())
a = int(input())
b = int(input())

if abs(x-a)==1 and abs(y-b)==2:
    print('YES')
elif abs(x-a)==2 and abs(y-b)==1:
    print('YES')
else:
    print('NO')