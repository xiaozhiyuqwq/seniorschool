number=input("在此输入一个五位数......")
jiance=["0","1","2","3","4","5","6","7","8","9"]
if len(number)!=5:
    print("您的输入非法！")
else:
    if number[0] in jiance and number[1] in jiance and number[2] in jiance and number[3] in jiance and number[4] in jiance:
        if number[0] == number[4] and number[1] == number[3]:
            print("您输入的",number,"是回文数！")
        else:
            print("您输入的",number,"不是回文数！")
    else:
        print("您的输入非法！")
#by xiaozhiyuqwq
