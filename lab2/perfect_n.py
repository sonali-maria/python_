" PERFECT NUMBER "

def fac_l(a):
	l_=[]
	if a<1:
		return None
	else:
		i=1
		while i<a:
			if a%i==0:
				l_.append(i)
			i=i+1
	return l_

num=int(input("enter the number to check if it a perfect number: "))
factor=fac_l(num)
sum1=0
for i in factor:
	sum1=sum1+i
if sum1==num:
	print("{} is a perfect number".format(num))
else:
	print("{} is not a perfect number".format(num))