#输入
h=float(input("在此输入您的身高(单位：米)......"))
w=float(input("在此输入您的体重(单位：千克)......"))
#计算BMI
BMI=w/(h**2)
#计算标准体重(SW)
SW=22*(h**2)
#输出
print("您输入的身高为",h,"米\n您输入的体重为",w,"千克。")
print("您的BMI指数为：",format(BMI,".2f"),"您的SW(标准体重)为：",format(SW,".2f"))
#判断BMI是否正常
if BMI>=16.5 and BMI<=22.7:
    print("您的BMI指数正常！")
else:
    print("您的BMI指数异常......")
#阿巴阿巴阿巴阿巴
#by xiaozhiyuqwq.top
#https://xiaozhiyuqwq.top
#Github:https://github.com/xiaozhiyuqwq
#Gitee:https://gitee.com/xiaozhiyuqwq
