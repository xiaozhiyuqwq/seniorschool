a=float(input("\n在此输入第一条边长\n\n"))
b=float(input("\n在此输入第二条边长\n\n"))
c=float(input("\n在此输入第三条边长\n\n"))
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)*0.5
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    print("\n\n\n该三角形的面积是 ",round(s,2)," \nP.S.自己去算单位")
else:
    print("\n\n\nERROR\n")
