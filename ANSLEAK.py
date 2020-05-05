def Reverse(lst): 
    new_lst = lst[::-1] 
    return new_lst 
import numpy as np
t = int(input())
for t in range(t):
	n,m,k =[int(n1) for n1 in input().split()]
	ans=[]
	for i in range(n):
		ans1 = []
		ans1 = [int(n2) for n2 in input().split()]
		ans.append(ans1)
	ans = np.array(ans)
	# print(ans)
	# ans= np.swapaxes(ans,0,1)
	ans2 = np.zeros((n))
	k1 = np.zeros((k))
	for i in range(len(ans)):
		index 		= 	np.where(k1 == np.amin(k1))
		index1 		= 	int(index[0][0])
		ans2[i]		= 	ans[i][index1]
		k1[index1] 	= 	((k1[index1]) + 1)
	ans2=ans2.astype(int)
	# ans2=Reverse(ans2)
	print(*ans2, sep =' ')
	# print(ans2)

