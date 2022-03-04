i=1
while i<=100:
	j=i
	sum=0
	while j>0:
		b=j%10
		sum=sum+b
		j=j//10
	if i %sum==0:
		print(i,'harsad no')
	else:
		print(i)
	i+=1
# 1 to 50 harshad number