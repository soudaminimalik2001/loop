num=int(input('enter number'))
i=1
f=0
while i<=num:
	if num%i==0:
			f+=1
	i+=1
if f==2:
	print('prime')
else:
	print('composit')