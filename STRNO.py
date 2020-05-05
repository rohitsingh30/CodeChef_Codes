import math
def primeFactors(n,count): 
	while n % 2 == 0: 
		# print (2)
		n = n / 2
		count = count+1
	for i in range(3,int(math.sqrt(n))+1,2): 
		while n % i== 0: 
			# print (int(i)) 
			n = int(n / i) 
			count = count+1
	if n > 2: 
		# print (int(n))
		count = count+1
	return count
t = int(input())
for t in range(t):
	x,k=[int(n) for n in input().split()]
	count =0 
	j = primeFactors(x,count)
	print(j)
	if j>=k:
		print(int(1))
	else:
		print(int(0))		
