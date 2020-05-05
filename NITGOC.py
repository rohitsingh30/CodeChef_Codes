t = int(input())
def result(x1,y1):
	if x1==y1:
		if x1!=1:
			print('NO')
			return None
		else:
			print('YES')
			return None
	else:
		if x1>y1:
			return(result(x1-y1,y1))
		else:
			return(result(x1,y1-x1))
for t in range(t):
	x,y=[int(n) for n in input().split()]
	result(x,y)