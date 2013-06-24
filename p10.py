import math

def is_prime(num):
	if num <= 1:
		return False
	if num == 2:
		return True
	if num % 2 == 0:
		return False
	m = int(math.sqrt(num))
	for i in range(3, m+1, 2):
		if num % i == 0:
			return False
	return True

sum = 0

# this could take a while...
for i in range(1, 2000001):
	print i
	if is_prime(i):
		sum += i

print sum
