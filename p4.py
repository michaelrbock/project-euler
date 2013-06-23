def is_palindrome(num):
	if str(num) == str(num)[::-1]:
			return True
	else:
		return False

largest = 0

for num1 in range(999, 99, -1):
	for num2 in range(999, 99, -1):
		num = num1 * num2
		if is_palindrome(num):
			if num > largest:
				largest = num

print largest