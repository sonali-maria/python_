" GUESSING THE NUMBER "

import random
l_limit=1
u_limit=100
num=random.randint(l_limit,u_limit)

print(" Guess game : where you guess the number ")
print()

while True:
	guess=int(input("guess the number between 1 to 100: "))
	print()
	if guess==num:
		print("your guess is correct! Number is {}".format(num))
		break
	else:
		if guess>num:
			print("WRONG! your number is greater than the actual number")
			print()
		else:
			print("WRONG! your number is smaller than the actual number")
			print()