x = int (input())
y = int(input())
a = int(input())
b = int(input())

if abs(a - x) == abs(b - y):
    print ('YES')
elif  x == a or y == b:
        print('YES')
else:
    print('NO')

