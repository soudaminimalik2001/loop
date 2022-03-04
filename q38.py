a=1
while a<=50:
	i=1
	sum=0
	while i<a:
		if a%i==0:
			sum+=i
		i+=1
	if sum==a:
		print(a,'perfect no')
	else:
		print(a)
	a+=1
# 1 to 50 perfect number