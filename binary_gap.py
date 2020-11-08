def solution(N):
	max_gap = 0
	gap = 0
	start_gap = False
	n = N
	while True:
		remain = n % 2
		if remain == 1:
			if start_gap:
				if gap > max_gap:
					max_gap = gap
				gap = 0
			else:
				start_gap = True
		if remain == 0 and start_gap:
			gap += 1
		n = n // 2
		if n == 0:
			break
	return max_gap

print(solution(1041))