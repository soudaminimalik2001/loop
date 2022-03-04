# Perfect number
a=int(input('enter number'))
sum=0
i=1
while i<a:
	if a%i==0:
		sum+=i
	i+=1
if sum==a:
		print(a,'is perfect number')
else:
		print(a,'is not perfect number')