def solution(A):
	total = sum(A)
	above_part = 0
	below_part = total
	min_diff = float('inf')
	for a in A[:-1]:
		above_part += a
		below_part -= a
		diff = abs(above_part - below_part)
		if min_diff > diff:
			min_diff = diff
	return min_diff

print(solution([1, 2, 3, 4, 2]))
