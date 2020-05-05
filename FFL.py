t = int(input())
for t1 in range(t):
	n,s=[int(n2) for n2 in input().split()]
	p=[int(n2) for n2 in input().split()]
	df=[int(n2) for n2 in input().split()]
	p1= []
	p0=[]
	for i in range(len(p)):
		if df[i]==1:
			p1.append(p[i])
		else:
			p0.append(p[i])
	p1=sorted(p1)
	p0=sorted(p0)
	if (len(p0)>0) and (len(p1)>0) :
		if ((p0[0]+p1[0])<=(100-s)):
			print('yes')
		else:
			print('no')
	else:
		print('no')
