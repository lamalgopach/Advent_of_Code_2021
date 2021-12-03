positions = {"forward" : (0, 1), "down" : (2, 1), "up" : (2, -1)}

coordinates = [0, 0, 0]
# horizontal, depth, aim

def which_dimension(course):
	return positions[course][0]

while True:
	try:
		command = input().split()

		course = command[0]
		x = int(command[1])
		
		dim = which_dimension(course) # 0 or 1 or 2
		coordinates[dim] += positions[course][1] * x
		if command[0] == "forward":
			coordinates[1] += coordinates[2] * x

	except EOFError:
		break
print(coordinates[0] * coordinates[1])



# First Part:
# positions = {"forward" : (0, 1), "down" : (1, 1), "up" : (1, -1)}

# coordinates = [0, 0]

# def which_dimension(course):
# 	return positions[course][0]

# while True:
# 	try:
# 		command = input().split()
# 		course = command[0]
#		x = int(command[1])
# 		dim = which_dimension(course) # 0 or 1
# 		coordinates[dim] += positions[course][1] * int(command[1])

# 	except EOFError:
# 		break
# print(coordinates[0] * coordinates[1])