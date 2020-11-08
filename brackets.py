def solution(S):
	stack = [""] * 100000
	size = 0
	for s in S:
		if s in ["(", "{", "["]:
			stack[size] = s
			size += 1
		elif s in ["]", "}", ")"]:
			size -= 1
			p = stack[size]
			if s == ")" and p != "(":
				return 0
			if s == "}" and p != "{":
				return 0
			if s == "]" and p != "[":
				return 0
	if size == 0:
		return 1
	else:
		return 0

print(solution("{[()(]}"))