import random
import time
import os
print("嘿，您好，您即将获得 5 秒钟的时间记忆物品及其编号！\n游戏即将开始！\n倒计时3\n\n\n*请不要输入两位数字！")
time.sleep(1)
os.system("cls")
print("嘿，您好，您即将获得 5 秒钟的时间记忆物品及其编号！\n游戏即将开始！\n倒计时2\n\n\n*请不要输入两位数字！")
time.sleep(1)
os.system("cls")
print("嘿，您好，您即将获得 5 秒钟的时间记忆物品及其编号！\n游戏即将开始！\n倒计时1\n\n\n*请不要输入两位数字！")
time.sleep(1)
os.system("cls")
print("游戏现在开始！\n\n\n\n\n*请不要输入两位数字！")
time.sleep(1)
os.system("cls")
things=["苹果","香蕉","橙子","梨子","猕猴桃","柚子",
"猴魁","铁观音","彩蛋","复活节"]
for i in range(10):
   print(i,":",things[i])
time.sleep(5)
os.system("cls")
n=0
t2=random.sample(things,5)
for i in t2:
    os.system("cls")
    print("*请不要输入两位数字！\n\n\n\n\n")
    ans=int(input(i + "的编号是:"))
    if i==things[ans]:
        n=n+1
os.system("cls")
print("\n您一共答对了 ",n," / 5 题。\n\n\n将于 5 秒后退出。")
time.sleep(1)
os.system("cls")
print("\n您一共答对了 ",n," / 5 题。\n\n\n将于 4 秒后退出。")
time.sleep(1)
os.system("cls")
print("\n您一共答对了 ",n," / 5 题。\n\n\n将于 3 秒后退出。")
time.sleep(1)
os.system("cls")
print("\n您一共答对了 ",n," / 5 题。\n\n\n将于 2 秒后退出。")
time.sleep(1)
os.system("cls")
print("\n您一共答对了 ",n," / 5 题。\n\n\n将于 1 秒后退出。")
time.sleep(1)
os.system("cls")
input("\n轻触回车键以退出。")
#对于教材的文件稍微改了一下
#python的特性导致不能输入两位数
#int=整数
#float=浮点数
#这两种均不可解决来自python的特性
#by xiaozhiyuqwq
#https://xiaozhiyuqwq.top
