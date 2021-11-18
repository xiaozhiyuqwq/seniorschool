#利率变化的余额
#设置本金
money=50000
#利率
rate=[0.0325,0.03,0.03,0.02,0.0175]
#循环
for i in rate:
    money=money*(1+i)
print("5年后的余额",money,"元。")
#by xiaozhiyuqwq
#https://www.rainyat.work
