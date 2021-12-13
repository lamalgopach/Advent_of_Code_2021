instructions = []
paper = {}
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
			if x not in paper:
				paper[x] = set()
			paper[x].add(y)
	except EOFError:
		break
for instruction in instructions:
	axis, fold = instruction.split("=")
	fold = int(fold)
	paper_after_folding = {}
	if axis == "x":
		for x, ys in paper.items():
			if x > fold:
				new_x = fold - abs(fold - x)
				if new_x not in paper_after_folding:
					paper_after_folding[new_x] = ys
				else:
					paper_after_folding[new_x].update(ys)
					
			elif x in paper_after_folding:
				paper_after_folding[x].update(ys)
			else:
				paper_after_folding[x] = ys

	elif axis == "y":
		for x, ys in paper.items():
			paper_after_folding[x] = set()
			for y in ys:
				if y > fold:
					new_y = fold - abs(fold - y)
					paper_after_folding[x].add(new_y)
				else:
					paper_after_folding[x].add(y)

	dots = 0
	for x, ys in paper_after_folding.items():
		dots += len(ys)
	paper = paper_after_folding

max_x, max_y = 0, 0
for k, v in paper_after_folding.items():
	max_x = max(max_x, k)
	max_y = max(max_y, max(v))

paper = []
for i in range(max_x + 2):
	lst = ["."] * (max_y + 1)
	paper.append(lst)

for x, ys in paper_after_folding.items():
	for y in ys:
		paper[x][y] = "#"


for line in paper:
	print(line)