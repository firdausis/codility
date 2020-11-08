def solution(X, Y, D):
	diff = Y-X
	if diff % D == 0:
		return diff // D
	else:
		return (diff // D) + 1
	

print(solution(0,91,30))
