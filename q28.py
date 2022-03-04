r=1
while r<=5:
	a=1
	while a<=5-r:
		print(' ',end=' ')
		a+=1
	c=1
	while c<=r:
		print('*',end=' ')
		c+=1
	print() 
	r+=1
# O/p:-
#            *
#          * *
#        * * *
#      * * * *
#    * * * * *