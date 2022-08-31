b = int(input()) 
s = 0

while s < b:
      if(b <= 10 ):
        s = s + b
        continue
      if(b >= 100):
       s = s + b
       break
       
print(s)