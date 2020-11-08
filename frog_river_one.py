def solution(X, A):
	s = set()
	for i,a in enumerate(A):
		s.add(a)
		if len(s) == X:
			return i
	return -1

A = [1, 3, 1, 4, 2, 3, 5, 4]
print(solution(1, A))

