drawn_numbers = list(map(int, input().split(",")))
blank = input()

def count_the_score(bingo, drawn_numbers):
	i, max_out = 0, 0
	x_lst, y_lst = [0] * 5, [0] * 5
	seen = set()

	while max_out < 5:
		if drawn_numbers[i] in bingo:
			x, y = bingo[drawn_numbers[i]][0], bingo[drawn_numbers[i]][1]
			x_lst[x] += 1
			y_lst[y] += 1
			max_out = max(max(x_lst), max(y_lst))
			seen.add(drawn_numbers[i])
		i += 1

	sum_unseen = 0
	for k, v in bingo.items():
		if k not in seen:
			sum_unseen += k

	return drawn_numbers[i - 1] * sum_unseen, i - 1

def check_score(winscore_first, winscore_second, score, j, i_min, i_max):
	if j < i_min:
		winscore_first = score
		i_min = j
	elif j > i_max:
		winscore_second = score
		i_max = j
	return winscore_first, winscore_second, i_max, i_min

bingo = {}
x = 0
i_max, i_min = 0, len(drawn_numbers)
winscore_first, winscore_second = 0, 0

while True:
	try:
		y_lst = list(map(int, input().split()))
		if y_lst:
			for i, num in enumerate(y_lst):
				bingo[num] = (x, i)
			x += 1
		else:
			score, j = count_the_score(bingo, drawn_numbers)
			winscore_first, winscore_second, i_max, i_min = check_score(winscore_first, winscore_second, score, j, i_min, i_max)
			x = 0
			bingo = {}
	except EOFError:
		break

score, j = count_the_score(bingo, drawn_numbers)
winscore_first, winscore_second, i_max, i_min = check_score(winscore_first, winscore_second, score, j, i_min, i_max)

print(winscore_first, winscore_second)