numbers = {2 : 1, 4 : 4, 3 : 7, 7 : 8}
count_numbers = 0
while True:
	try:
		[entry, output] = input().split("|")
		for code in output.split():
			if len(code) in numbers:
				count_numbers += 1

	except EOFError:
		break
print(count_numbers)