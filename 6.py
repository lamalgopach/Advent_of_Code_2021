lanternfish_school = list(map(int, input().split(",")))

# Part 2:
def count_fish(lanternfish_school, days):
	fish_dict = {}

	for fish in lanternfish_school:
		if fish not in fish_dict:
			fish_dict[fish] = 0
		fish_dict[fish] += 1

	for day in range(days):
		next_day_fish = {}
		for days, fish in fish_dict.items():
			if days == 0:
				if 6 in next_day_fish:
					next_day_fish[6] += fish
				else:
					next_day_fish[6] = fish
				next_day_fish[8] = fish
			elif days - 1 not in next_day_fish:
				next_day_fish[days - 1] = fish
			else:
				next_day_fish[days - 1] += fish
		fish_dict = next_day_fish


	sum_of_fish = 0
	for day, fish in fish_dict.items():
		sum_of_fish += fish

	return sum_of_fish

print(count_fish(lanternfish_school, 256))




# Part 1:
# def count_lanterfish(days, lanternfish_school):
# 	for day in range(days):
# 		new_fish = 0
# 		for i, fish in enumerate(lanternfish_school):
# 			if fish == 0:
# 				new_fish += 1
# 				lanternfish_school[i] = 6
# 			else:
# 				lanternfish_school[i] -= 1
# 		for fish in range(new_fish):
# 			lanternfish_school.append(8)
# 	return len(lanternfish_school)

# print(count_lanterfish(80, lanternfish_school))
