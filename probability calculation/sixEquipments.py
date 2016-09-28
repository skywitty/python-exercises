#!/usr/bin/python3
#encoding:UTF-8
import math
import random
# 装备名列表（数组）
equipments = ['阿什坎迪', '霜之哀伤', '灰烬使者', '埃辛诺斯战刃', '影之哀伤', '阿契厄斯']

# 玩家抽中的装备集合，集合的元素唯一性。这里用字典来存储，字典的key为装备名，value为抽中的状态，初始值都为0
ownersE = {'阿什坎迪': 0, '霜之哀伤':0, '灰烬使者': 0, '埃辛诺斯战刃':0, '影之哀伤': 0, '阿契厄斯':0}

# 实验次数，默认值设为100
testTimes = 100

# 抽奖次数
tryTimes = 0

# 所有实验中抽奖次数总和
tryTimesTotal = 0

# 这里也可以用列表来记录玩家是否抽中装备,数组长度为6，初始值全为0
# 如果抽中某件装备则将对应序列值改成1
ownersList = [0, 0, 0, 0, 0, 0]
print("每次抽奖都能抽中一件装备的实验结果如下：")
while testTimes>0:
	while math.fsum(ownersList)<6:
		# 开始抽奖
		# 1到6的随机整数，与装备名一一对应
		r = random.randint(0,5)
		# 对装备集合进行处理
		ownersList[r] = 1
		tryTimes = tryTimes + 1
	else :
		print("第",(100-testTimes),"次实验结果：抽奖",tryTimes,"次")
		tryTimesTotal = tryTimesTotal + tryTimes
		# print(tryTimes)
		tryTimes = 0
		ownersList = [0, 0, 0, 0, 0, 0]
	testTimes = testTimes - 1
else :
	print("实验结束")
	print(testTimes)

print("当每次抽奖都能抽中一件装备时的实验结果，抽奖次数平均值：",tryTimesTotal/100)

tryTimesTotal = 0
testTimes = 100
# 有可能是抽中装备的概率为1/6，至于抽中哪件装备则随机
# 即有可能不能抽中
print("抽中装备的概率为1/6，至于抽中哪件装备则随机的实验结果如下：")

while testTimes>0:
	while math.fsum(ownersList)<6:
		# 开始抽奖
		# 1到6的随机整数，与装备名一一对应
		r = random.randint(0,5)
		# 是否抽中，当随机数是1时抽中，否则不抽中
		isornot = random.randint(1,6)
		if isornot == 1:
			# 对装备集合进行处理
			ownersList[r] = 1
		tryTimes = tryTimes + 1
	else :
		print("第",(100-testTimes),"次实验结果：抽奖",tryTimes,"次")
		tryTimesTotal = tryTimesTotal + tryTimes
		# print(tryTimes)
		tryTimes = 0
		ownersList = [0, 0, 0, 0, 0, 0]
	testTimes = testTimes - 1
else :
	print("实验结束")
	print(testTimes)

print("抽中装备的概率为1/6，至于抽中哪件装备则随机的实验结果，抽奖次数平均值：",tryTimesTotal/100)
