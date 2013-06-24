def is_prime(num):
	for i in range(2, num):
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
