x = float(input())
y = float(input())
z = str(input())

if (z == 'mod' and y != 0):
    print(x % y)
if (z == 'mod' and y == 0):
    print('Деление на 0!')
if (z == 'pow'):
    print(x ** y)
if (z == 'div' and y!=0.0):
    print(x // y)
if (z =='div' and y == 0):
    print('Деление на 0!')
if (z == '+'):
    print(x + y)
if (z == '-'):
    print(x - y)
if (z == '*'):
     print(x * y)
if (z == '/' ):
    print(x / y)
