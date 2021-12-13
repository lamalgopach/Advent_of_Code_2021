octopi = []

while True:
	try:
		line = str(input())
		line_of_octopi = [int(a) for a in line]
		octopi.append(line_of_octopi)
	except EOFError:
		break

# INCREASING - first phase of the step:
def increase_energy_by_one(octopi):
	to_visit = set()
	for i, line in enumerate(octopi):
		for j, octopus in enumerate(line):
			octopi[i][j] += 1
			if octopi[i][j] > 9:
				to_visit.add((i, j))
	return octopi, to_visit

# range checker:
def is_in_octopus_range(x, y, octopi):
	return 0 <= x < len(octopi) and 0 <= y < len(octopi[0])

# helper function to the second part:
def increase_adjacent(i, j, octopi, visited, to_visit):
	coordinates = [(-1, -1), (-1, 0), (-1, 1), 
					(0, -1),           (0, 1), 
				    (1, -1),  (1, 0),  (1, 1)]
	for xy in coordinates:

		x, y = i + xy[0], j + xy[1]

		if is_in_octopus_range(x, y, octopi) and (x, y) not in visited:
			if octopi[x][y] < 10:
				octopi[x][y] += 1
				if octopi[x][y] > 9 and (x, y) not in visited:
					to_visit.add((x, y))
	return octopi, to_visit, visited

# second part:
def increase_the_energy_level_of_adjacent(octopi, to_visit):
	visited = set()

	while to_visit:
		i, j = to_visit.pop()
		visited.add((i, j))
		octopi, to_visit, visited = increase_adjacent(i, j, octopi, visited, to_visit)

	return octopi

# flashing:
def zero_octopi_above_nine(octopi):
	for i, line in enumerate(octopi):
		for j, octopus in enumerate(line):
			if octopi[i][j] > 9:
				octopi[i][j] = 0
	return octopi
# count flashes:
def count_flashes(octopi):
	new_flashes = 0
	all_flashing = False
	for line in octopi:
		for octopus in line:
			if octopus == 0:
				new_flashes += 1
	if new_flashes == len(octopi) * len(octopi[0]):
		all_flashing = True
	return new_flashes, all_flashing

steps = 1
flashes = 0
all_flashing = False
flashes_after_100_steps = 0

while not all_flashing:

	new_flashes = 0
	octopi, to_visit = increase_energy_by_one(octopi)
	octopi = increase_the_energy_level_of_adjacent(octopi, to_visit)
	octopi = zero_octopi_above_nine(octopi)
	new_flashes, all_flashing = count_flashes(octopi)
	flashes += new_flashes
	if steps == 100:
		flashes_after_100_steps = flashes
	steps += 1
	print("after step", steps - 1)
	for line in octopi:
		print(line)
	print()
print(flashes_after_100_steps)
print(steps - 1)


