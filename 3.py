gamma, epsilon = "", ""

a = 0
frequency = {}
nums = []

while True:
	try:
		num = input()
		a += 1
		for i, n in enumerate(num):
			if i not in frequency:
				frequency[i] = 0
			if n == "1":
				frequency[i] += 1
		nums.append(num)

	except EOFError:
		break


for k, v in frequency.items():
	if v > a // 2:
		gamma += "1"
		epsilon += "0"
	elif v < a // 2:
		gamma += "0"
		epsilon += "1"

gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)

print(gamma_int * epsilon_int)

oxy, co2 = [], []
oxygen_gen_rating, co2_scrub_rating = "", ""

def determine_values(nums, lst, common, i):
	for num in nums:
		if num[i] == common:
			lst.append(num)
	return lst

if gamma[0] == "1":
	oxy = determine_values(nums, oxy, "1", 0)
	co2 = determine_values(nums, co2, "0", 0)
else:
	oxy = determine_values(nums, oxy, "0", 0)
	co2 = determine_values(nums, co2, "1", 0)

def count_frequency(lst, pos, most):

	zeros, ones = 0, 0
	for i, num in enumerate(lst):
		if num[pos] == "0":
			zeros += 1
		else:
			ones += 1

	if most:
		return "0" if zeros > ones else "1"
	else:
		return "0" if zeros <= ones else "1"


def count_ratings(lst, most):
	i = 1

	while i < len(lst[0]) and len(lst) > 1:
		stays = count_frequency(lst, i, most)
		lst = determine_values(lst, [], stays, i)
		i += 1

	return lst[0]

oxygen_gen_rating = count_ratings(oxy, True)
co2_scrub_rating = count_ratings(co2, False)

print(int(oxygen_gen_rating, 2) * int(co2_scrub_rating, 2))












