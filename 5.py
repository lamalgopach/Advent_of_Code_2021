mtx = []
for i in range(1000):
	line = ["."] * 1001
	mtx.append(line)
overlap = 0

while True:
	try:
		k = input().replace(" -> ", ",").split(",")
		x0, y0, x1, y1 = int(k[0]), int(k[1]), int(k[2]), int(k[3])

		dx, dy = x1 - x0, y1 - y0
		
		step_x = dx // abs(dx)if dx != 0 else 0
		step_y = dy // abs(dy) if dy != 0 else 0


		steps_to_go = max(abs(dx), abs(dy))

		x, y = x0, y0
		while steps_to_go >= 0:	
			if mtx[x][y] == ".":
				mtx[x][y] = 1
			elif mtx[x][y] == 1:
				overlap += 1
				mtx[x][y] += 1
			x, y = x + step_x, y + step_y
			steps_to_go -= 1

	except EOFError:
		break
print(overlap)





# Part 1:

# mtx = []
# for i in range(1000):
# 	line = ["."] * 1000
# 	mtx.append(line)
# overlap = 0

# while True:
# 	try:
# 		k = input().replace(" -> ", ",").split(",")
# 		x1, y1, x2, y2 = int(k[0]), int(k[1]), int(k[2]), int(k[3])

# 		if x1 == x2:
# 			a = y1 if y1 < y2 else y2
# 			b = y2 if y1 < y2 else y1
# 			for i in range(a, b + 1):
# 				if mtx[x1][i] == ".":
# 					mtx[x1][i] = 1
# 				elif mtx[x1][i] == 1:
# 					overlap += 1
# 					mtx[x1][i] += 1
# 		elif y1 == y2:
# 			a = x1 if x1 < x2 else x2
# 			b = x2 if x1 < x2 else x1

# 			for i in range(a, b + 1):
# 				if mtx[i][y1] == ".":
# 					mtx[i][y1] = 1
# 				elif mtx[i][y1] == 1:
# 					overlap += 1
# 					mtx[i][y1] += 1
			
# 	except EOFError:
# 		break
# print(overlap)
