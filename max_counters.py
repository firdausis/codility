def solution(N, A):
	imax = 0
	vmax = 0
	counter = [0] * N
	for a in A:
		if a == N + 1:
			if vmax < counter[imax]:
				vmax = counter[imax]
				counter = [vmax] * N
		else:
			counter[a - 1] += 1
			if counter[imax] < counter[a-1]:
				imax = a - 1
	return counter

A = []
print(solution(5, A))
