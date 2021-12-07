positions = list(map(int, input().split(",")))

def count_fuel(num):
	fuel = 0
	for i in range(1, num + 1):
		fuel += i
	return fuel

crabs = {}
for crab in positions:
	if crab not in crabs:
		crabs[crab] = 0
	crabs[crab] += 1

# crabs' positions range:
start, end = min(positions), max(positions)

min_first = len(positions) * abs(start - end)
max_fuel = count_fuel(len(positions))
min_second = len(positions) * abs(start - end) * max_fuel

fuel_dict = {}

for pos in range(start, end + 1):
	cost_first, cost_second = 0, 0

	for crab_pos, num in crabs.items():
		if abs(pos - crab_pos) not in fuel_dict:
			fuel = count_fuel(abs(pos - crab_pos))
			fuel_dict[abs(pos - crab_pos)] = fuel
		cost_first += (abs(pos - crab_pos)) * num
		cost_second += fuel_dict[abs(pos - crab_pos)] * num

	min_first = min(min_first, cost_first)
	min_second = min(min_second, cost_second)
print(min_first)
print(min_second)