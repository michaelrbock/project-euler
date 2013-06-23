number = 2520

while True:
	all = True
	for i in range(20, 0, -1):
		if number % i != 0:
			number += i - number % i
			all = False
	if (all):
		break

print number