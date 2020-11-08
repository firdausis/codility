def solution(A):
	vmax = max(A)
	counter = {} 
	for a in A:
		if a in counter:
			counter[a] += 1
		else:
			counter[a] = 1
	for i in range(1, vmax+1):
		if (i not in counter) or (counter[i] > 1):
			return 0
	return 1

A = [1, 1]
print(solution(A))
