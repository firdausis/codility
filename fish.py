def solution(A,B):
	stack = []
	n_fish = len(A)
	n_eaten = 0

	for a,b in zip(A,B):
		if b == 1:
			stack.append(a)
		else:
			while len(stack) > 0:
				n_eaten += 1
				if a > stack[-1]:
					stack.pop()
				else:
					break
	
	return n_fish - n_eaten

A = [4, 3, 2, 1, 5]
B = [1, 0, 0, 0, 0]
print(solution(A,B))