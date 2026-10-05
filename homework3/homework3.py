# --- Homework 3 ---

# --- 3 Print Functions ---

# 3.1 say goodbye

def say_goodbye(name):
	print("Goodbye," , name)

name = "olivia" 
say_goodbye("olivia")

# 3.2 area of a circle 

def calc_a(r):  # calculates area of a circle
	print(3.14*(r**2))

r = "2"
calc_a(2)

# --- 4 Return Functions ---
def subtract(a, b): #subtracts
	print(a - b)

a = 10
b = 7
subtract(10, 7)

def multiply(a, b): #multiplies
	print(a * b)

multiply(a, b)

def divide(a, b): #divides
	print(a / b)

b = 2
divide(a, b)

# --- 5 conditionals ---

# 5.1 what to wear 
def what_to_wear(temps):
	return(min(temps), max(temps))

temps = [64, 78, 83, 94, 67, 87,]

print(what_to_wear(temps))

# 5.2 is it weekend 

def check_weekend(day):
	if day == 6 or day == 7:
		return True
	else:
		return False

print(check_weekend(3))

# 5.3 fuel efficietcy 
def fuel_eff(dist, fuel):
	return dist / fuel

print(fuel_eff(100, 5))

# 5.4 Secret code 
def secret_code(x):
	ending = x % 10
	rest = x // 10
	return ending * 10000 + rest

print(secret_code(12345))

# --- 6 Loops ---

# 6.1 oski stole your power 
def power(a, b):
	result = 1

	for i in range(b):
		result = result * a

	return result 

print(power(3, 3))

# 6.2 min and max 
# 6.2.1 for loops

def min(numbers):
	smallest = numbers[0]

	for num in numbers:
		if num < smallest:
			smallest = num

	return smallest

numbers = [14, 76, 67, 48, 24, 12, 94]

print(min(numbers))

def max(numbers):
	largest = numbers[0]

	for num in numbers:
		if num > largest:
			largest = num

	return largest

print(max(numbers))

# 6.2.2 while loops 

def minimum(numbers):
	smallest = numbers[0]
	i = 1

	while i < len(numbers):
		if numbers[i] < smallest:
			smallest = numbers[i]
		i += 1

	return smallest 

print(minimum(numbers))

def maximum(numbers):
	largest = numbers[0]
	i = 1

	while i < len(numbers):
		if numbers[i] > largest:
			largest = numbers[i]
		i += 1

	return largest 

print(maximum(numbers))

# 6.3 calculate the sum 

def sum(numb):
	total = 0

	while numb > 0:
		digit = numb % 10
		total = total + digit
		numb = numb // 10 

	return total 

numb = 2468
print(sum(numb))

	














