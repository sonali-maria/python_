" ATM "

bal=50000.00
c_pin="123456"

def pin_check():
	x=input("ENTER YOUR PIN CODE: ")
	if x==c_pin:
		return True
	else:
		return False
	

ch='y'
while ch=='y' or ch=="Y":
	print("=====WELCOME=====")
	print("MAIN MENU")
	print("1. CHECK BALANCE ")
	print("2. DEPOSIT")
	print("3. WITHDRAW")
	print("4. EXIT")
	choice=int(input("ENTER YOUR CHOICE: "))

	if choice==1:
		if pin_check():
			print("YOUR BALANCE: ",bal)
		else:
			print("WRONG PIN")
	elif choice==2:
		if pin_check():
			amount=float(input(" ENTER THE DEPOSIT AMOUNT: "))
			if amount>0:
				bal=bal+amount
				print("CURRENT BALANCE: ",bal)
			else:
				print("CURRENT BALANCE: ",bal)
		else:
			print("WRONG PIN")
	elif choice==3:
		if pin_check():
			amount=float(input(" ENTER THE WITHDRAWAL AMOUNT: "))
			if amount>0:
				bal=bal-amount
				print("CURRENT BALANCE: ",bal)
			else:
				print("CURRENT BALANCE: ",bal)
		else:
			print("WRONG PIN")
	elif choice==4:
		print("THANK YOU FOR VISTING ")
		ch='n'
	else:
		print("INVALID OPTION")