###Prime bumber.....
n=int(input("enter any number"))
i=1
f=0
while i<=n:
	if n%i==0:
		f=f+i
	i=i+1
if i%2==0:
	print("prime num")
else:
	print("nit")