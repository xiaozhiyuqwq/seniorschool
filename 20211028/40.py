#列表创建
spring=[3,4,5]
summer=[6,7,8]
autumn=[9,10]
autumn.append(11)
winter=[12,1,2,3]
winter.remove(3)
#输入
month=int(input("请输入一个月份......"))
#判断输入
if month in spring:
    print("您输入的",month,"是春天！")
elif month in summer:
    print("您输入的",month,"是夏天！")
elif month in autumn:
    print("您输入的",month,"是秋天！")
elif month in winter:
    print("您输入的",month,"是冬天！")
else:
    print("无效的输入") 
#by xiaozhiyuqwq
#https://xiaozhiyuqwq.top
