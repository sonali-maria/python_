def addition(a,b):
	return a+b
def sub(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	if (b!=0):
		return a/b
	else:
		return "2nd number shouldn't be zero for this evaluation!"

def cal():
	ch="y"
	while ch=='y'or ch=="y":
		a=int(input("enter your 1st number :"))
		b=int(input("enter your 2nd number :"))
		print("1:to add")
		print("2:to subtract")
		print("3:to multiply")
		print("4:to divide")
		print("5:to exit")
		choice=int(input("enter your choice: "))
		if choice==1: 
			print(addition(a,b))
		elif choice==2: 
			print(sub(a,b))
		elif choice==3: 
			print(multiply(a,b))
		elif choice==4: 
			print(divide(a,b))
		else:
			ch='no'
		ch=input("enter y to continue :")

cal()