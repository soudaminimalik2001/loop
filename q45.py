n=int(input('enter number'))
a=n
sum=0
while n>0:
	sum=sum+(n%10)**3
	n=n//10
if a==sum:
	print('armstrong')
else:
	print('not armstrong')