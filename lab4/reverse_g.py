" REVERSE GUESS GAME "

a=int(input("enter the number: "))
low=0
high=100
while True:
	mid=(low+high)//2
	ch=input("the guess is: {} (LOWER/HIGHER/CORRECT)".format(mid))
	if ch=="LOWER" or ch=="lower":
		high=mid
	elif ch=="HIGHER" or ch=="higher":
		low=mid
	else:
		break
