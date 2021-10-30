foodlist1=["apple","pizza","salad"]
foodlist2=["apple","icecream"]
while True:
    food=input("输入一个食物吧！")
    if food in foodlist1 and food in foodlist2:
        print("好耶！食物",food,"是我们都想吃的！")
        break
    elif food in foodlist1 and food not in foodlist2 or food not in foodlist1 and food in foodlist2:
        print("啊嗷！食物",food,"有一个人不想吃。")
    else:
        print("啊嗷！食物",food,"我们都不想吃。")
#by xiaozhiyuqwq
#https://xiaozhiyuqwq.top