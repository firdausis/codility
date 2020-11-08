def solution(A):
	n = len(A)
	max_slice_end = [0] * n
	max_sum = 0
	for i in range(1, n - 1):
		a = A[i]
		max_sum = max(0, max_sum + a)
		max_slice_end[i] = max_sum

	max_slice_start = [0] * n
	max_sum = 0
	for i in range(n - 2, 1, -1):
		a = A[i]
		max_sum = max(0, max_sum + a)
		max_slice_start[i] = max_sum
	
	# print(max_slice_end)
	# print(max_slice_start)

	max_double_slice = max_slice_end[0] + max_slice_start[2]
	for i in range(1, n - 1):
		max_double_slice = max(max_double_slice, max_slice_end[i - 1] + max_slice_start[i + 1])
		# print(max_double_slice)

	return max_double_slice

A = [0] * 8
A[0] = 3
A[1] = 2
A[2] = 6
A[3] = -1
A[4] = 4
A[5] = 5
A[6] = -1
A[7] = 2
print(solution(A))
