instructions = []
paper = {}
dots_set = set()
while True:
	try:
		data = input()
		if not data:
			continue
		if data[0] == "f":
			data = data.strip("fold along ")
			instructions.append(data)

		else:
			data = data.split(",")
			x, y = int(data[0]), int(data[1])
			dots_set.add((x, y))
	except EOFError:
		break

for instruction in instructions:
	axis, fold = instruction.split("=")
	fold = int(fold)
	paper_after_folding = {}
	new_dots_set = set()
	for dot in dots_set:
		if axis == "x" and dot[0] > fold:
			new_x = fold - abs(dot[0] - fold)
			new_dots_set.add((new_x, dot[1]))
		elif axis == "y" and dot[1] > fold:
			new_y = fold - abs(dot[1] - fold)
			new_dots_set.add((dot[0], new_y))
		else:
			new_dots_set.add(dot)
	dots_set = new_dots_set
	dots = len(dots_set)
	print(dots)

max_x, max_y = 0, 0
for dot in dots_set:
	max_x, max_y = max(max_x, dot[0]), max(max_y, dot[1])

paper = [["."] * (max_y + 1) for i in range(max_x + 2)]

for dot in dots_set:
	x, y = dot[0], dot[1]
	paper[x][y] = "#"

for line in paper:
	print(line)
# 71 -> 49