numbers = {2 : 1, 4 : 4, 3 : 7, 7 : 8}

#  AAA
# B   C
# B   C
#  DDD
# E   F
# E   F
#  GGG

def determine_number_negative(entry, letter):
	num_to_define = ""
	for num in entry:
		if letter not in num:
			num_to_define = num
			entry.remove(num)
			break
	return num_to_define, entry

def determine_number_positive(entry, letter):
	num_to_define = ""
	for num in entry:
		if letter in num:
			num_to_define = num
			entry.remove(num)
			break
	return num_to_define, entry

def decode_entry(entry):
	C, F = "", ""
	one, four, seven, eight = entry[2], entry[4], entry[3], entry[7]
	numbers = {}
	numbers[one], numbers[four], numbers[seven], numbers[eight] = "1", "4", "7", "8"

	# determine 6 and C
	six_or_nine_or_zero = entry[6]
	six = ""

	six, nine_or_zero = determine_number_negative(six_or_nine_or_zero, one[0])
	if not six:
		six, nine_or_zero = determine_number_negative(six_or_nine_or_zero, one[1])
	numbers[six] = "6"
	C = one[0] if one[0] not in six else one[1]

	# determine F:
	F = one[0] if one[0] != C else one[1]

	# determine 2, 3 and  5
	two, three, five = "", "", ""
	two_or_three_or_five = entry[5]

	two, three_or_five = determine_number_negative(two_or_three_or_five, F)
	numbers[two] = "2"

	three, set_five = determine_number_positive(three_or_five, C)
	numbers[three] = "3"
	five, rest = determine_number_positive(set_five, F)
	numbers[five] = "5"

	# determine B and D
	b_or_d = ""
	for letter in four:
		if letter not in one:
			b_or_d += letter
	for letter in two:
		if letter in b_or_d:
			D = letter
			B = b_or_d[0] if D == b_or_d[1] else b_or_d[0]
			break

	# determine 9 and 0
	for num in nine_or_zero:
		if D not in num:
			zero = num
			numbers[zero] = "0"
		else:
			nine = num
			numbers[nine] = "9"
	# print(numbers)
	return numbers

def decode_numbers(entry, output):
	numbers = decode_entry(entry)
	count = ""
	output = output.split()
	for num in output:
		for code, number in numbers.items():
			if set(code) == set(num):
				count += number
				break
	return int(count)

count_numbers = 0
count_second = 0
while True:
	try:
		[entry, output] = input().split("|")
		entry = entry.split()
		new_entry = {}
		for code in entry:
			if len(code) not in new_entry:
				new_entry[len(code)] = ""
				new_entry[len(code)] = code
			elif type(new_entry[len(code)]) == str:
				last = new_entry[len(code)]
				new_entry[len(code)] = set()
				new_entry[len(code)].add(last)
				new_entry[len(code)].add(code)
			else:
				new_entry[len(code)].add(code)
		entry = new_entry
		for code in output.split():
			if len(code) in numbers:
				count_numbers += 1
		count_second += decode_numbers(entry, output)

	except EOFError:
		break
print(count_numbers)
print(count_second)
