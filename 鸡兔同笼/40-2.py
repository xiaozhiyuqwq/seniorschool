#鸡兔同笼
print('这是一个有关鸡兔同笼的问题')
heads=int(input('请输入总头数:'))
legs=int(input('请输入总脚数:'))
for tu in range(1,heads-1):
    leg=4*tu+2*(heads-tu)
    if leg == legs:
        print('兔子有:',tu,'头')
        print('鸡有:',int(heads-tu),'头')
input("运行完成，请轻敲回车键退出......")
#by xiaozhiyuqwq
#https://xiaozhiyuqwq.top
