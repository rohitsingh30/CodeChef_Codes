t = int(input())
import numpy as np
for t1 in range(t):
	n=int(input())
	x=int(input())
	n1=[int(n2) for n2 in input().split()]
	n1=np.array(sorted(n1))
	index = np.arange(0,n/x,n/x)
	a1 = np.subtract(n1,index)
	if a1[0]<=1:
		print('Impossible')
	else:
		print('Possible')