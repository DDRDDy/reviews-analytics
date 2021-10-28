reviews = [] #留言清單
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		reviews.append(line)

sum_lenth = 0
for review in reviews:
	sum_lenth = sum_lenth + len(review) 
	#sum_lenth += len(review)

average = sum_lenth / len(reviews) #留言平均長度
print('留言平均長度為', average)
