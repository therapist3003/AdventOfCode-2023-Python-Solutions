res = 0

with open('2.txt', 'r') as file:
	line_index = 0
	for line in file:
		line_index += 1
		rounds = [round for round in (line.split(':')[1]).split(';')]
		max_blue, max_red, max_green = 0,0,0
		for round in rounds:
			blue, red, green = 0,0,0
			for item in str(round).split(','):
				color = str(item).split()[1]
				count = int(str(item).split()[0])
				if color == 'blue':
					blue += count
				elif color == 'red':
					red += count
				elif color == 'green':
					green += count
			max_blue = max(max_blue, blue)
			max_red = max(max_red, red)
			max_green = max(max_green, green)

		if max_red>12 or max_green>13 or max_blue>14:
			continue
		else:
			res += line_index

print(res)

