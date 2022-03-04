i=1
c=0
while c<=50:
	f=0
	j=1
	while j<=i:
		if i%j==0:
			f+=1
		j+=1
	if f==2:
		print(i)
	c+=1
	i+=1
# 1 to 50 prime numbers