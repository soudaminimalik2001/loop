a=int(input('enter number'))
r=0
while a>0:
	r=(r*10)+a%10
	a=a//10
	b=r+a
if a%b==0:
	print(a,'is a harshad number')
else:
	print('not')