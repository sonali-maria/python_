" PALINDROME NUMBER "

num=int(input("enter any number to check if it is palindrome : "))

sum1=0
a=num
while a>0:
	digit=a%10
	sum1=sum1*10+digit
	a=a//10
if sum1==num:
	print("{} is a palindrome number".format(num))
else:
	print("{} is not a palindrome number".format(num))
