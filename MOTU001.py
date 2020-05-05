t = int(input())
for t in range(t):
	a,b,c=[int(n) for n in input().split()]
	remainder = c%a
	if remainder>b:
		x = c - abs(b-remainder)
	elif remainder<b:
		x = c - (a-abs(b-remainder)) 
	else:
		x= c	
	print(x)
