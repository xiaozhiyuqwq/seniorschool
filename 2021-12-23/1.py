#初始化
t=0
#运算
for x in range(1,9):
    for y in range(1,11):
        for z in range(1,13):
            if 6*x+5*y+4*z==50:
                print("计算出x值为 ",x," y值为 ",y," z值为 ",z," 。")
                t=t+1
print("计算出一共有 {} 个结果。".format(t))
#by xiaozhiyuqwq
#https://www.rainyat.work
#2021-12-23
