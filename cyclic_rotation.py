def solution(A, K):
	if A==[]:
		return A
	K = K % len(A)
	if K==0:
		return A
	return A[-K:] + A[:len(A)-K]

print(solution([], 0))
