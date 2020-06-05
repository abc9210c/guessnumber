import random

p = random.randint(1, 100)
count = 0
while True:
	count += 1
	num = input('猜猜數子: ')
	num = int(num)
	if num == p:
		print('你猜對了!!')
		break
	elif num > p:
		print('比答案大')
	elif num < p:
		print('比答案小')
	print('這是猜的第', count, '次')