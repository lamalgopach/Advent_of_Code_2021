opened = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}
error_scores = {")" : 3, "]" : 57, "}" : 1197 , ">" : 25137 }

autocomplete_tool = {")" : 1, "]" : 2 , "}" : 3 , ">" : 4 }

error_score = 0
total_scores = []

while True:
	try:
		corrupted = False
		line = input()
		open_lst = []

		for l in line:
			if l in opened:
				open_lst.append(l)
			elif l == opened[open_lst[-1]]:
				open_lst.pop()
			elif l != opened[open_lst[-1]]:
					error_score += error_scores[l]
					corrupted = True
					break

		if not corrupted:
			total_score = 0

			for i in range(len(open_lst) - 1, -1, -1):
				total_score *= 5
				total_score += autocomplete_tool[opened[open_lst[i]]]

			total_scores.append(total_score)
	except EOFError:
		break

print(error_score) # part 1
total_scores.sort()
i = len(total_scores) // 2

print(total_scores[i]) # part 2

