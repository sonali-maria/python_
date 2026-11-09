" ARMSTRRONG NUMBER"

num=int(input("enter the number to check if it is armstrong number: "))

sum1=0
a=num
p=len(str(num))

while a>0:
	digit=a%10
	sum1=sum1+(digit**p)
	a=a//10
if (sum1==num):
	print("yes, {} is armstrong number".format(num))
else:
	print("no, {} is not an armstrong number".format(num))