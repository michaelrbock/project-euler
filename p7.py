def is_prime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

count = 1
number = 3

while True:
	if is_prime(number):
		count += 1
		if count == 10001:
			break
	number += 1


print number