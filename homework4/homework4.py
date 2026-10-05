# --- 3 Lists ---

# 3.1 List Operations 

food = ["bread", "sushi", "eggs", "pasta", "pretzels"]

print(food[1])

print(food[::-1])

food.append("cookie")

food.insert(0, "apple")

del food[2]

print(len(food))

new_food = food[0::len(food)-1]
print(new_food)

if "potato" in food:
    print("A potato!")
else: 
    print("No potato!")

# for food in food2:
#     print(food.upper()) # got an error here for using wrong syntax

# 3.2 Slicing and Striding 

numbers = list(range(21))

def get_first_15(numbers):
    return numbers[:15]

def get_every_fifth(step1):
    return step1[::5]

def reverse_and_stride(step1):
    reversed_list = step1[::-1]
    return reversed_list[::3]

step1 = get_first_15(numbers)
step2 = get_every_fifth(step1)
step3 = reverse_and_stride(step2)

print(step3)

# 3.3 Nested lists

# # 3.3.1 nested list operations 

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(numbers[2])

print(numbers[1][1])

numbers.append([10, 11, 12])
print(numbers)

def sum_nested(numbers):
    total = 0
    for row in numbers:
        for number in row:
            total += number
    return total   # error here for not returning a number

print(sum_nested(numbers))

# 3.4 create a 5x5 list 

def create_list():  # create 5x5 list
    result = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        result.append(row)

    return result 


def replace_3(step1):  #replace multiples of 3 with ?
    for i in range(5):
        for j in range(5):
            if step1[i][j] % 3 == 0:
                step1[i][j] = "?"
    return step1


def sum(step1): # sum everything not ?
    total = 0
    for i in range(5):
        for j in range(5):
            if step1[i][j] != "?":
                total += step1[i][j]
    return total

step1 = create_list()
step2 = replace_3(step1)
step3 = sum(step2)

print(step3)

# 4 Dictionaries 

# 4.1 Dictionary Operations

ages = {"Katie": 30, "Mariam": 42, "Safia": 25, "Mira": 48}

print(ages["Katie"])

ages["Mira"] = 100

ages["Milana"] = 35

del ages["Mariam"]

for name, age in ages.items():
    print(f"{name} = {age}")

print(ages.items())










    



