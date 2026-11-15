" STUDENT GRADE CALCULATOR "

marks=[]
sub=["MATH","ENGLISH","HINDI","EVS","SST"]
i=1
sum1=0
while i<6:

	try:
		a=int(input("ENTER YOUR {} MARKS: ".format(sub[i-1])))
		if a>0 and a<100:
			marks.append(a)
		else:
			print("INVALID DATA ")
	except:
		print("INVALID DATA TYPE")
		break;

	sum1=sum1+marks[i-1]
	i=i+1
avg=sum1/5
if avg>=90:
	print("A GRADE")
elif avg>=80 and avg<90:
	print("B GRADE")
elif avg>=70 and avg<60:
	print("C GRADE")
if avg>=60 and avg<50:
	print("D GRADE")
else:
	print("FAIL")