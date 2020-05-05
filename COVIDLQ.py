t = int(input())
for i in range(t):
	count=0
	n = int(input())
	k = []
	index=[]
	s=[int(j) for j in input().split()]
	for w in range(n):
		k.append(s[w])
	for v in range(len(k)):
		if k[v]==1:
			index.append(v)
	for a in range(len(index)):
		for b in range(len(index)):
			if a>b:
				diff = abs(index[a]-index[b])
				if diff<6:
					count=1
	if count == 1:
		print('NO')
	else:
		print('YES')
