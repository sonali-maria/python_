"PRIME NUMBER"

def c_prime(a):
	if a<=1:
		return False
	else:
		if a==2:
			return True
		else:
			i=2
			while i<a:
				if a%i==0:
					return False
				i=i+1
			return True

a=int(input("enter your lower limit: "))
b=int(input("enter your upper limit: "))

p_list=[]

while a<=b:
	if c_prime(a):
		p_list.append(a)
	a=a+1

print("The list is: {}".format(p_list))