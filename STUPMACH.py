def pointer(s,j,count1):
	count2=0
	if j+1<=len(s):
		if s[j]<=s[j+1]:
			pointer(s,j+1,count1)
		else:
			return decrease(s,j,count1,count2)
def decrease(s,j,count1,count2):
	for k in range(j):
		if s[k]==0:
			count1=1
		else:
			s[k]=s[k]-1
			count2=count2+1
	return count2
t = int(input())
for i in range(t):
	count=0
	count1=0
	j=0
	n=int(input())
	s=([None]*n)
	s=[int(n) for n in input().split()]
	for it in range(5*(10**6)):
		if count1!=1:
			count=count+pointer(s,j,count1)
print(count)
