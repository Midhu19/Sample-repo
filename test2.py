x=[1,2,3,4,5,6,7,"a"]
x.remove(x[len(x)-1])
for y in range(1,len(x)):
    if y%2==0:
        x.remove(y)
        
print(x)