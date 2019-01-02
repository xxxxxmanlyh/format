import time

datetime = time.strftime('%Y年%m月%d日',time.localtime(time.time()))
print("名字：")
name = input()
print("动态钱包美元：")
missUSD = input()
print("静态钱包美元：")
rewardUSD = input()
print("扣除推荐奖：")
losttuijian = input()
print("获得推荐奖")
gettuijian= input()
rewardRMB = float(rewardUSD) * 6.8
allUSD = float(missUSD) + float(rewardUSD)

print(datetime)
print("姓名:"+name)
if int(losttuijian) >0 and int(gettuijian) >0:
    missRMB = (float(missUSD) - int(losttuijian)+int(gettuijian)) * 6.8
    print("分享收益:(" + str(missUSD) +"-"+str(losttuijian)+"+"+str(gettuijian)+")＄*6.8=" + str(int(missRMB)) + "元")
    allUSD = float(missUSD) + float(rewardUSD) - int(losttuijian)+int(gettuijian)
elif int(losttuijian) == 0 and int(gettuijian) >0:
    missRMB = (float(missUSD)  + int(gettuijian)) * 6.8
    print("分享收益:(" + str(missUSD)  + "+" + str(gettuijian) + ")＄*6.8=" + str(int(missRMB)) + "元")
    allUSD = float(missUSD) + float(rewardUSD)  + int(gettuijian)
elif int(losttuijian) >0 and int(gettuijian) == 0:
    missRMB = (float(missUSD) - int(losttuijian)) * 6.8
    print("分享收益:(" + str(missUSD) + "-" + str(losttuijian)  + ")＄*6.8=" + str(int(missRMB)) + "元")
    allUSD = float(missUSD) + float(rewardUSD) - int(losttuijian)
else:
    missRMB = float(missUSD) * 6.8
    print("分享收益:" + str(missUSD) + "＄*6.8=" + str(int(missRMB)) + "元")
    allUSD = float(missUSD) + float(rewardUSD)
print("理财收益:"+str(rewardUSD)+"＄*6.8="+str(int(rewardRMB))+"元")
print("总计:（"+str(allUSD)+"美金)×6.8=("+str(int(missRMB+rewardRMB))+")人民币")
# print("("+str(allUSD)+"美金)×6.8=("+str(int(missRMB+rewardRMB))+")人民币")
