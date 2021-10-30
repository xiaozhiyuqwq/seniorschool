#检测是否是数字
jiance=["0","1","2","3","4","5","6","7","8","9"]
#进行循环
while True:
    number=input("在此输入一个五位数......")
    if len(number)!=5:
        print("您的输入非法！ERRORREASON:请输入一个五位自然数......")
    else:
        if number[0] in jiance and number[1] in jiance and number[2] in jiance and number[3] in jiance and number[4] in jiance:
            #是回文数
            if number[0] == number[4] and number[1] == number[3]:
                print("您输入的",number,"是回文数！")
                break
            else:
                print("您输入的",number,"不是回文数！")
        else:
            print("您的输入非法！ERRORREASON:严禁输入非阿拉伯数字！")
#by xiaozhiyuqwq
#https://xiaozhiyuqwq.top