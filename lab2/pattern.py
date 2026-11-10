" PATTERN PRINTING "

print(" THE STAR PATTERN ")
for i in range(1,6):
	for j in range(1,i+1):
		print("*",end=" ")
	print()


print(" THE HALF PYRAMID WITH NUMBER ")
for i in range(1,6):
	for j in range(1,i+1):
		print(j,end=" ")
	print()

print(" THE REVERSE PYRAMID ")
for i in range(1,6):
	for j in range(1,6-i):
		print("*",end=" ")
	print()

print(" THE SQUARE ")
for i in range(1,6):
	for j in range(1,6-i):
		print("*",end=" ")
	for k in range(1,i+1):
		print("*",end=" ")
	print()

print(" THE RIGHT ANGLED TRIANGLE ")
for i in range(1,6):
	for j in range(1,6-i):
		print(" ",end=" ")
	for k in range(1,i+1):
		print("*",end=" ")
	print()
print(" THE CENTER PYRAMID ")
for i in range(1,6):
	for j in range(1,6-i):
		print(" ",end=" ")
	for k in range(1,2*i):
		print("*",end=" ")
	print()