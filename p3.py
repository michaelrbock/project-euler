largest = 0
factor = 2
number = 600851475143

def is_prime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

while (number > 1):
	if number % factor == 0:
		number = number / factor
		if factor >largest and is_prime(factor):
			largest = factor
		factor = 2
	else:
		factor += 1

print largest