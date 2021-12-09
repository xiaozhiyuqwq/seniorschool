def F(x):
    s=1
    for i in range(2,x+1):
        s=s*i
    return s
sum=1
for i in range(2,11):
    sum=sum+F(i)
print("1!+2!+3!……+10!是",sum)
    
