def solution(A):
	counter = {}
	for a in A:
		if a in counter:
			counter[a] += 1
		else:
			counter[a] = 1
	for k,v in counter.items():
		if v % 2 == 1:
			return k

print(solution([9,3,9,3,9,7,9]))
