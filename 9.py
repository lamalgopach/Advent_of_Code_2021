big_basin = []

while True:
	try:
		row = input()
		big_basin.append(row)
	except EOFError:
		break

def is_in_range(x, y, big_basin):
	return 0 <= x < len(big_basin) and 0 <= y < len(big_basin[0])

def are_points_around_lower(i, j, big_basin):
	field, lower_points = 0, 0

	coordinates = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	small_basin = []
	small_basin_set = set()

	for c in coordinates:
		x, y = i + c[0], j + c[1]

		if is_in_range(x, y, big_basin):
			field += 1
			
			if big_basin[i][j] < big_basin[x][y]:
				lower_points += 1
				if big_basin[x][y] != 9:
					small_basin.append((x, y))
					small_basin_set.add((x, y))
					small_basin_set.add((i, j))

	return lower_points == field, small_basin, small_basin_set

def count_basin_size(i, j, big_basin):
	basin_set = set()
	basin_set.add((i, j))
	yes_no, basin, b_set = are_points_around_lower(i, j, big_basin)
	if basin:
		basin_set.update(b_set)
		for b in basin:
			print(basin)
			yes_no, b2, bs = are_points_around_lower(b[0], b[1], big_basin)
			for b in bs:
				if b not in basin_set:
					basin.append(b)

	return len(basin_set)


risks_level = 0
three_largest_basins = []

for i, row in enumerate(big_basin):
	for j, point in enumerate(row):

# 				i-1,j == A
# i,j-1 == B	i,j 			i,j+1 == C
# 				i+1,j == D
	
		around_lower, lst, basin_set = are_points_around_lower(i, j, big_basin)
		if around_lower:
			risks_level += int(point) + 1	

			three_largest_basins.append(count_basin_size(i, j, big_basin))
			print(i, j, three_largest_basins)
print(risks_level)

three_largest_basins.sort()
print(three_largest_basins)
print(three_largest_basins[-1] * three_largest_basins[-2] * three_largest_basins[-3])	



# 789892
# 896789
# 965678



