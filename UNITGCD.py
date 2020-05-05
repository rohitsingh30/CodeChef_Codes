import math 
def is_prime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
import timeit
import numpy as np
t = int(input())
for a in range(t):
	x3=[]
	x4=[]
	n = int(input())
	start = timeit.default_timer()
	x2=[]
	for j1 in range(1,n+1):
		if (j1==2 or j1%2!=0):
			x = is_prime(j1) 
			if x:
				x2=[]
				x2 = np.arange(0,n+1,j1)
				# print(x3)
				if not n/j1<2: 
					x2 = np.delete(x2,x3)
					# print(x3)
					x2= x2[1:]
					x3 = np.concatenate((x3, x2))
					# x3 = np.sort(x3)
					x3 = x3.astype(int)
				else:
					x2=x2[1:]
				x2 = np.array(x2)
				x4.append(x2)
	# print(x4.shape)
	print(len(x4[0]))
	index1=0
	count2=-1
	for k in range(len(x4)):
		count2=count2+1
		a1 = x4[k][0]
		count3=1
		for k1 in range(len(x4[k])-2):
			if k1!=0:
				a2=gcd(a1,x4[k][k1+1])
				if a2==1:
					count3=count3+1
					a1=a1*x4[k][k+1]
				else:
					x4[count2]=x4[:count3]
					x4[count2+1]=np.concatenate(x4[count2+1],x4[count3:])
	for k in range(len(x4[0])):
		index1=index1+1
		count = 0
		count1=[]
		if k==0:
			for j in range(len(x4)):
				if (len(x4[j])-1)>=k:
					count=count+1
					count1.append(x4[j][k])
			count1 = [1] + count1
			print(*([count]+count1), sep =' ')
		else:
			for j in range(len(x4)):
				if (len(x4[j])-1)>=k:
					count=count+1
					count1.append(x4[j][k])
			print(*([count]+count1), sep =' ')
