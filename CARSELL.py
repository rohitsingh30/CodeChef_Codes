import numpy as np
t = int(input())
for i in range(t):
	n = int(input())
	p = [int(p1) for p1 in input().split()]
	p = sorted(p,reverse =True)
	for k in range(len(p)):
		p[k] = p[k]-k 
		if p[k]<=0:
			p[k]=0
	sum1 = np.sum(p)
	print(sum1%1000000007)