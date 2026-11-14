" MATRIX OPERATIONS "

" TO MAKE THE MATRIX"
a=int(input("enter the number of rows you want: "))
b=int(input("enter the number of columns you want: "))

matrix=[]
for i in range(0,a):
	row=[]
	for j in range(0,b):
		row.append(int(input("enter the number for {} row's {} column: ".format(i+1,j+1))))
	matrix.append(row)

" TO SHOW MATRIX "
for i in range(0,a):
	print("[",end="")
	for j in range(0,b):
		print(matrix[i][j], end="  ")
	print("]")

" second way to print the matrix"
for i in matrix:
	print(i)

" TO SHOW SUM OF ALL ELEMENTS AND SUM OF DIAGONALS "
sum1=0
d_sum=0
for i in range(0,a):
	for j in range(0,b):
		sum1=sum1+matrix[i][j]
		if i==j:
			d_sum=d_sum+matrix[i][j]
print("The sum of all elements is : {} and sum of diagonals : {}".format(sum1,d_sum))

" TO show the transpose of the matrix "
m=[]
for i in range(b):
	row=[]
	for j in range(a):
		row.append(0)
	m.append(row)

" or could use m[[0]*a for j in range(b) : to make the nested list]"		
for l in range(0,a):
	for k in range(0,b):
		m[k][l]=matrix[l][k]
for i in m:
	print(i)