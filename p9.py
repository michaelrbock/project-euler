save = (0,0,0)

for a in range(1, 999):
	if save != (0,0,0):
		break
	for b in range(1, 999):
		for c in range(1, 999):
			if (a + b + c) == 1000:
				if a*a + b*b == c*c:
					save = a,b,c

print save[0]*save[1]*save[2]