def solution(S, P, Q):
	factor = { 'A': 1, 'C': 2, 'G': 3, 'T': 4}
	min_factor = {}
	for i,s in enumerate(S):
		min_factor[(i,i)] = factor[s]
		for j,s2 in enumerate(S[i+1:]):
			min_factor[(i,j)] = min(factor[s2], min_factor[(i,j-1)]
	print(min_factor)

print(solution(['CAGCCTA'],None,None))
