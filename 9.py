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
	basin, lower_points = 0, 0
	coordinates = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	basin_area = set()
	basin_area.add((i, j))
	to_visit = set()

	# part 1:
	for c in coordinates:
		x, y = i + c[0], j + c[1]

		if is_in_range(x, y, big_basin):
			basin += 1
			if big_basin[i][j] < big_basin[x][y]:
				lower_points += 1

				if int(big_basin[x][y]) != 9:
					basin_area.add((x, y))
					to_visit.add((x, y))
	# part2:
	while to_visit:
		i, j = to_visit.pop()

		for c in coordinates:
			x, y = i + c[0], j + c[1]

			if is_in_range(x, y, big_basin) and int(big_basin[x][y]) < 9:
				if (x, y) not in basin_area:
					basin_area.add((x, y))
					to_visit.add((x, y))

	return lower_points == basin, len(basin_area), basin_area

risks_level = 0
three_largest_basins = []

for i, row in enumerate(big_basin):
	for j, point in enumerate(row):

		around_lower, basin, basin_area = are_points_around_lower(i, j, big_basin)
		if around_lower:
			risks_level += int(point) + 1	
			three_largest_basins.append(basin)

print(risks_level)
three_largest_basins.sort()
print(three_largest_basins[-1] * three_largest_basins[-2] * three_largest_basins[-3])	