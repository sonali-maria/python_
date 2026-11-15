" GUESS GAME WITH HINT "
import random

num=random.randint(1,100)
attempt=0
max_a=10

print(" rules:")
print("1: you will only get 10 chances to guess the number")
print("2: we will tell you two hint")
 

print()
even_o_odd="even" if num%2==0 else "odd"
multiple_of_5="divisible by 5" if num%5==0 else "not divisible by 5"
print("HINT 1: {}".format(even_o_odd))
print("HINT 2: {}".format(multiple_of_5))

while attempt<10:
	try:
		guess=int(input("enter your guess: "))
	except:
		print("Invalid input")
		continue

	attempt+=1
	score=(max_a-attempt)*10

	if guess==num:
		print("CORRECT! AND YOUR SCORE IS: {}".format(score))
		break
	print("WRONG GUESS! USE HINT")
	print("ATTEMPT LEFT: {}".format(max_a-attempt))
else:
	print("KO! GAME OVER! NUMBER IS {}".format(num))