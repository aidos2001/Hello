n = int(input())


if ( 1 <= n and  n <=10  or  n % 10 ):
    print(n, 'программист')
if ((n % 100) // 10 ):
    print(n, 'программистов')
if ((n % 1000) ):
    print(n, 'программистов')
