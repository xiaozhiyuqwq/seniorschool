#回文数
allnumber=["1","2","3","4","5","6","7","8","9","0"]
while True:
    number=str(input("在此输入一个五位数......"))
    if len(number)==5:
        if number[0]!=0:
            if number[0] in allnumber and number[1] in allnumber and number[2] in allnumber and number[3] in allnumber and number[4] in allnumber:
                if number[0]==number[4] and number[1]==number[3]:
                    print("您输入的 {} 是回文数。".format(number))
                    break
                else:
                    print("您输入的 {} 不是回文数。".format(number))                    
            else:
                print("您输入的 {} 不是一个数字。".format(number))
        else:
            print("您输入的 {} 不属于数字(首位不可为0)。".format(number))
    else:
        print("您输入的数字 {} 不属于五位数。".format(number))
