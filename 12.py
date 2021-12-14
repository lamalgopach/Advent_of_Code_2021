steps = {}

while True:
	try:
		c1, c2 = input().split("-")
		if c1 not in steps:
			steps[c1] = []
		if c2 != "start":
			steps[c1].append(c2)
		if c2 not in steps:
			steps[c2] = []
		if c1 != "start":
			steps[c2].append(c1)
	except EOFError:
		break

del steps["end"]

def can_go_to_small_cave(prefix):
	caves = set()
	for c in prefix:
		if c.islower():
			if c in caves:
				return False
			else:
				caves.add(c)
	return True

def find_paths_second(cave, steps, prefix, more_time_paths):
	caves = steps[cave]
	for cave in caves:
		if cave == "start":
			continue
		elif cave == "end":
			p = prefix + ("end", )
			more_time_paths.add(p)
			# prefix = ()
		elif cave.islower() and cave in prefix:
			if can_go_to_small_cave(prefix):
				p = prefix + (cave, )
				find_paths_second(cave, steps, p, more_time_paths)
			else:
				continue
		# elif cave.islower() and not can_go_to_small_cave(prefix):
		# 	continue
		else:
			p = prefix + (cave, )
			find_paths_second(cave, steps, p, more_time_paths)

	return paths

def find_paths(cave, steps, prefix, paths):
	caves = steps[cave]
	for cave in caves:
		if cave == "start" or (cave.islower() and cave in prefix):
			continue
		elif cave != "end":
			p = prefix + (cave, )
			find_paths(cave, steps, p, paths)
		elif cave == "end":
			p = prefix + ("end", )
			paths.add(p)
	return paths

paths = set()
more_time_paths = set()
for n, cave in enumerate(steps["start"]):
	prefix = ("start", cave, )
	paths.update(find_paths(cave, steps, prefix, paths))
	more_time_paths.update(find_paths_second(cave, steps, prefix, more_time_paths))

print(len(paths))
print(len(more_time_paths))