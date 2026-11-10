" FIBONACCI SERIES "

num=int(input("enter the number of digits you want of fibonacci series"))
list1=[1]

i=1

last=1
second_l=0
while i<num:
	list1.append(last+second_l)
	last=list1[-1]
	second_l=list1[-2]
	i=i+1
print(list1)