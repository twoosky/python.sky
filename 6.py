x = int(input("x : "))
y = int(input("y : "))

i=1
result=0
while i<x and i<y:
    if x%i==0 and y%i==0:
        result=i
    i+=1

print(i)
