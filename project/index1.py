a = str(input())
pi  = 3.14


if ( a == 'прямоугольник' ):
    b = float(input())
    c = float(input())
    print(b * c)
if ( a == 'треугольник'):
    b = float(input())
    c = float(input())
    r = float(input())
    s = (b + c + r) /2 
    print((s*(s-b)*(s-c)*(s-r)) ** 0.5)
if (a == 'круг' ):
    c = float(input())
    print(pi * c ** 2)

