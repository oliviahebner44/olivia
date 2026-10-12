# --- 2 Homework 1 + 2 Review 
#  2.1 Vocab Revwiew 

# 1. git is local to keep track of changes, github is a remote platform to save projects 
# 2. terminal is where you write code, commandline is text based interface 
# 3. local repo is on your comuter, remote is on a server
# 4. version control is a system to track changes and restore previous versions 
# 5. staging area is where you add changes you want to save in the next commit 
# 6. git add adds changes to the staging area
# 7. git commit saves the staged changes to local repo
# 8. git push stores local chommit to remote repo
# 9. git status shows status of current directory and staging area
# 10. git pull downloads changes from remote repo and adds then to local branch
# 11. pwd print working directory 
# 12. ls list all the files and directories
# 13. cd changes your directory to another directory 
# 14. nano edits a text file in ther terminal
# 15. touch creates a new file 
# 16. mv moves a file or renames it 
# 17. rm deletes a file 
# 18. cat shows the contentc of a file 

# 2.2 Directory Tree 
# Questions 
# 1. pwd 
# 2. ls
# 3. cd ~/python_decal/brianna_repo
# git pull 
# 4. mv ~/python_decal/brianna_repo/homework.py ~/python_decal/judy_decal/homework/
# 5. cd ~/python_decal/brianna_repo
# 6. cat homework.py
# 7. git add . 
# git commit -m "finished homework"
# git push origin main 
# 8. remote repo has changes that local doesn't, so she needs to call git pull again 
# git pull 
# git push origin main 
# 9. cd ../../Recent

# --- Homework 3 Review ---
# 3.1 Data Types 

def checkDataType(num):
    return type(num).__name__

print(checkDataType(6.7))

print(checkDataType(True))

# 3.2 Conditionals 

def evenOrOdd(num0):
    if num0 % 2 ==0:
        return "Even"
    else:
        return "Odd"

print(evenOrOdd(7))

print(evenOrOdd(10))

# 4 Loops 

def sumWithLoop(numbers):
    start = 0
    for num in numbers:
        start += num
    return start 

numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))

# 5. Homework 4 Review 

# 5.1 Lists 
def duplicateList(lst):
    newlist = []
    for item in lst:
        newlist.append(item)
        newlist.append(item)
    return newlist    

lst = ['a', 'b', 'c']
print(duplicateList(lst))

# 5.3 Debugging 
# there was no semicolon after defining the function
def square(num):
    return num * num
print(square(5))
