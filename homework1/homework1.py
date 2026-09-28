# File : homework1.py

# --- Variables and Data Types ---

a = 10 
print(a)
print(type(a)) # a in an integer, a whole number with no decimals 

b = 1.5 
print(b)
print(type(b)) # b is a float, a number with a decimal 

c = 3j
print(c)
print(type(c)) # c is a complex, mix of number and variable 

d = "hello"
print(d)
print(type(d)) # is a string, list of characters 

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, an order of items 

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary with corresponding values 

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, with a specific order 

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list like e but with words 

i = True 
print(i)
print(type(i)) # i is a boolean, true or false 

j = None
print(j)
print(type(j)) # j is a nonetype, no value 

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list which can conatin different data types 

l = str(14)
print(l)
print(type(l)) # l is a string and converts 14 into text 

m = 1e4
print(m)
print(type(m)) # m is a float, written in scientific notation 

# --- Questions ---
# 1. i found 9 different data types 
# 2. integer, float, complex, string, list, dictionary, tuple, boolean, nonetype, 
# 3. m and b, l and d, k and h and e
# 4. l is a string not an integer because str() prints the number into a text. 
# n = {"blue", "red", "yellow"}
# print(n)
# print(type(n)) n is a set, an unordered collection of values 

# --- Boolean ---

print(10>9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, any non-empty string is considered True in a boolean context
print(bool(123)) # True, any non-zero number is considered True in a boolean context
print(bool(["apple", "cherry", "banana"])) # True, any non-empty list is considered True in a boolean context
print(bool(True)) # True, the boolean value is true 
print(bool(False)) # False, the boolean value is false 
print(bool(0)) # False, zero is considered False 
print(bool("")) # False, an empty string is considered False
print(bool(" ")) # True, a non-empty string with spaces is considered True
print(bool(())) # False, an empty tuple is considered False
print(bool([])) # False, an empty list is considered False
print(bool({})) # False, an empty dictionary is considered False
print(bool(True and False)) # False, the result of True and False is False
print(bool(True and True)) # True, the result of True and True is True
print(bool(False and False)) # False, the result of False and False is False
print(bool(True or False)) # True, the result of True or False is True
print(bool(True or True)) # True, the result of True or True is True
print(bool(False or False)) # False, the result of False or False is False
print(bool(True or False)) # True, the result of True or False is True
print(bool(False or False)) # False, the result of False or False is False
print(bool(not(False))) # True, the result of not(False) is True
print(bool(not(True))) # False, the result of not(True) is False

# --- Questions ---
# 1. if the function is given a value and not left empty then it will return as true 
# 2. I was suprised about the zero being false 
# 3. print(bool(67)) # True, any non-zero number is considered True in a boolean context
# 4. print(bool(10 == 11)) # False, 10 is not equal to 11


# --- Operators --- 

# Arithmatic Operators 
print(10 + 5) # 15, performs addition 
print(10 -5) # 5, performs subtraction 
print(2 * 4) # 8, performs multiplication 
print(6 / 3) # 2, performs division 
print(5 % 2) # 1, performs modulo operation (remainder of division)
print(3 ** 2) # 9, performs exponentiation 
print(15 // 2) # 7, performs floor division (integer division)

# Comparison Operators 
print(5 == 2) # False, 5 is not equal to 2
print(10 != 10) # False, 10 is equal to 10
print(2 < 5) # True, 2 is less than 5
print(12 > 5) # True, 12 is greater than 5
print(5 <= 6) # True, 5 is less than or equal to 6
print(1 >=10) # False, 1 is not greater than or equal to 10

# Assignments Operators 
x = 5 # assigns the value 5 to the variable x

x += 5
print(x) # 10, adds 5 to 5 

x -= 4
print(x) # 6, subtracts 4 from 10

x *= 3 
print(x) # 18, multiplies 6 by 3

# --- Logical Operators ---
# 1. the operator and takes into consideration both and returns True if both operands are True, otherwise False
# print(True and True) # True, the result of True and True is True
# print(True and False) # False, the result of True and False is False
# 2. the operator or takes into consideration both and returns True if at least one of the operands is True, otherwise False
# print(True or False) # True, the result of True or False is True
# print(False or False) # False, the result of False or False is False  
# 3. the operator not takes into consideration the operand and returns the opposite boolean value
# print(not(True)) # False, the result of not(True) is False
# print(not(False)) # True, the result of not(False) is True    

# --- More Questions ---
# 1. / is division and // is integer division 
# 2. % gives the remainder and // gives the integer part of the division
# 3. print(7 % 3) # 1, the remainder of 7 divided by 3
# 4. assignment operators asign or update the value of a variable 


# --- Strings --- 
my_string = "hello"
print(my_string) # hello 
print(my_string[0]) # h, the first character of the string
print(my_string[1]) # e, the second character of the string
print(my_string[2]) # l, the third character of the string
print(my_string[3]) # l, the fourth character of the string
print(my_string[4]) # o, the fifth character of the string  
print(my_string[-1]) # o, the last character of the string
print(my_string[1:3]) # el, the substring from index 1 to 3 (not including 3)
print(my_string[0:5:2]) # hlo, the substring from index 0 to 5 with a step of 2
print(len(my_string)) # 5, the length of the string
print(my_string + "goodbye") # hellogoodbye, concatenates the two strings
print(my_string * 7) # hellohellohellohellohellohellohello, repeats the string 7 times

# --- Questions --- 
# slicing is where you pick out only a part of a sequence like line 158 and 159 
# name = "Oski"
# print("Hello, my name is", name)  # Hello, my name is Oski
# name = "Oski"
# print(f"Hello, my name is {name
# print(f"Hello, my name is {name}")  # Hello, my name is Oski 
# 4. The last print is an f string which makes it easier to insert variables into a string 


# --- Terminal Commands ---

# 1. cd 
# changes directories. use it to move from one folder to another 
# example: cd Desktop 
# 2. ls
# lists files and directories in the current directory
# example: ls Desktop
# 3. ls -a
# lists all files and directories, including hidden ones
# example: ls -a
# 4. mkdir
# creates a new directory
# example: mkdir NewFolder
# 5. cat
# displays the contents of a file
# example: cat filename.txt
# 6. pwd
# prints the current working directory
# example: pwd
# 7. cd ..
# changes to the parent directory
# example: cd ..
# 8. cd . 
# changes to the current directory (does nothing)
# example: cd .
# 9. cd ~
# changes to the home directory
# example: cd ~ 
# 10. cp
# copies files or directories
# example: cp filename.txt NewFolder/
# 11. mv
# moves or renames files or directories
# example: mv filename.txt NewFolder/
# 12. rm
# removes files or directories
# example: rm filename.txt  
# 13. clear
# clears the terminal screen
# example: clear
# 14. grep 
# searches for text within files
# example: grep "text" filename.txt

# --- Questions --- 
# 15. find
# searches for files and directories based on criteria
# example: find . -name "*.txt" 
# 16. touch
# creates an empty file or updates the timestamp of an existing file
# example: touch filename.txt   
# 17. chmod
# changes the permissions of a file or directory
# example: chmod 755 filename.txt   

#2. ls -s shows all the hidden files 
#3. a hidden file is a file that starts with a dot (.) and is not shown by default when listing files in a directory
#4. -l used with ls gives more details abou files, -r used with ls reverses the order of files, -R used with ls to recursively list contentcs

