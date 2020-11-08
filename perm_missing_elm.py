def solution(A):
	if len(A)==0:
		return 1
	s = set(A)
	for i in range(1,len(A)+2):
		if i not in s:
			return i
	

print(solution([1,4,2]))
