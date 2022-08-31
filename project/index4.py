s = int(input())
if (s >= 0):
    if(s ==0):
        print(str(s) + "программистов")
    elif (s%100 >= 10 and s%100 <=20):
        print(str(s) + "программистов")
    elif(s%10==1):
        print(str(s) + "программист")
    elif (s%10 >=1 and s%10 <=4):
        print(str(s) + "программиста")
    else:
        print(str(s) + "программистов")
    
