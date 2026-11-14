" STAR PATTERN"

a=int(input("enter the number of rows you want: "))

" NORMAL STAR PATTERN "
for i in range(1,a+1):
	for j in range(1,i+1):
		print("*",end="")
	print()

print()
" A RIGHT ANGLED STAR PATTERN "
for i in range(1,a+1):
	for j in range(1,i+1):
		print(" ",end="")
	for k in range(a-i+1,0,-1):
		print("*",end="")
	print()
