number=input("在此输入一个五位数......")
if len(number)!=5:
    number=input("您的输入非法！\n在此重新输入一个五位数......")
elif number[0] == number[4] and number[1] == number[3]:
    print("您输入的",number,"是回文数！")
else:
    print("您输入的",number,"不是回文数！")
#by xiaozhiyuqwq
