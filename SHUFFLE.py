import numpy as np 
t = int(input())
for t1 in range(t):
	n,k=[int(n2) for n2 in input().split()]
	a=[int(n2) for n2 in input().split()]
	a=np.array(a)
	sort_index = np.argsort(a) 
	print(sort_index)
	sort_index1 = np.argsort(-1*a) 
	b = np.arange(0,n,1)
	c = abs(sort_index-b)
	c1 = abs(sort_index1-b)
	c = c%k
	c1 = c1%k
	if ((not np.any(c)) and (not np.any(c1))):
		print('yes')
	else:
		print('no')		