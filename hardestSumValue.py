t = int(raw_input())
while t:
	t-=1	
	arr = []
	n,m = map(int, raw_input().split())
	for i in range(n):
		arr.append(map(int, raw_input().split()))

	left,right,up,down = [],[],[],[]
	for i in range(n):
		temp = []
		for j in range(m):
			temp.append(0)
		left.append(temp[:])
		right.append(temp[:])
		up.append(temp[:])
		down.append(temp[:])
	#left

	for i in range(n):
		left[i][0] = arr[i][0]
		for j in range(1,m):
			left[i][j] = min(arr[i][j], arr[i][j]+ left[i][j-1])
	# right
	for i in range(n):
		right[i][-1] = arr[i][-1]
		for j in range(m-2, -1,-1):
			right[i][j] = min(arr[i][j], arr[i][j]+ right[i][j+1])
	# up
	for i in range(m):
		up[0][i] = arr[0][i]
		for j in range(1,n):
			up[j][i] = min(arr[j][i], arr[j][i]+ up[j-1][i])
	for i in range(m):
		down[-1][i] = arr[-1][i]
		for j in range(n-2,-1,-1):
			down[j][i] = min(arr[j][i], arr[j][i]+ down[j+1][i])

	final = []
	for i in range(n):
		temp = []
		for j in range(m):
			temp.append(up[i][j]+left[i][j]+right[i][j]+down[i][j] - 3*arr[i][j])
		final.append(temp)
	ans = []
	for i in final:
		ans.append(min(i))
	print min(ans)
