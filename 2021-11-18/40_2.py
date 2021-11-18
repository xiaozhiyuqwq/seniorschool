#指数增长
s=0
for i in range(30):
    s=s+2**i
    print("天数",i,"当前数值",s)
print(s)
