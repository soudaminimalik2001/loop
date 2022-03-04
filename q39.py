a=int(input('enter number'))
sum=0
n=a
while n>0:
	i=1
	f=1
	r=n%10
	while i<=r:
		f=f*i
		i+=1
	sum+=f
	n=n//10
if sum==a:
	print(a,'strong number')
else:
	print('not a strong')