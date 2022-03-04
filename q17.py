i=1
sum=0
avg=0
while i<=11:
				a=int(input("enter weight"))
				sum=sum+a
				i+=1
				avg=sum/10
print(sum)
print(avg)
if avg%5==0:
				print(avg,"is divisible by 5")
else:
				print(avg,"not divisible by 5")