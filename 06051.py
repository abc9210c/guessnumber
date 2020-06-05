import random

p = random.randint(1, 100)
while True:
	num = input('猜猜數子: ')
	num = int(num)
	if num == p:
		print('你猜對了!!')
		break
	else:
	    if num != p and num < p:
	    	print('你猜錯囉!!')
	    	print('比答案小')
	    elif num != p and num > p:
	        print('你猜錯囉!!')
	        print('比答案大')	
            

	    

