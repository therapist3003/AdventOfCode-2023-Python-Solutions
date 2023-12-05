res = 0

with open('2.txt', 'r') as file:
	for line in file:
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

		res += max_blue*max_green*max_red

print(res)

