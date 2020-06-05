import random

p = random.randint(1, 100)
while True:
	num = input('猜猜數子: ')
	num = int(num)
	if num == p:
		print('你猜對了!!')
		break
	elif num > p:
		print('比答案大')
	elif num < p:
		print('比答案小')