
current, last = None, None
increased = 0
m = []
while True:
	try:
		last = current
		current = int(input())
		m.append(current)
		if last:
			if current > last:
				increased += 1

	except EOFError:
		break
# print(increased)

current_sum, last_sum = None, None
increased_sum = 0

for i in range(2, len(m)):
	if current_sum:
		last_sum = current_sum
	current_sum = sum(m[i - 2:i + 1])
	if last_sum:
		if current_sum > last_sum:
			increased_sum += 1

print(increased_sum)


	



