def Area(x,y,z):
    if x+y>z and x+z>y and y+z>x:
        p=(x+y+z)*0.5
        s=(p*(p-x)*(p-y)*(p-z))**0.5
        return s
    else:
        print("Error")
A=Area(18,22,17)+Area(25,22,36)+Area(18,14,13)+Area(36,10,32)+Area(18,15,32)
print("多边形的面积是 ",round(A,2)," 。")
