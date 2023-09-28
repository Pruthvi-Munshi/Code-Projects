# Comparison operators - only return booleans (true or false)
# == Equal to
# != Not equal to
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to

# Boolean operators
# true / false
# TRUTH TABLES GO HERE
# print(True and True) -> True
# print(True and Flase) -> False
# print(Flase and True) -> False
# print(Flase and Flase) -> False

# print(True or True) -> True
# print(True or Flase) -> True
# print(Flase or True) -> True
# print(Flase or Flase) -> False

# not opperator
# print(not True) -> false

# if statements
# if (this is true):
# perform these actions - actions outside of indentation will happen no matter what
true_one = True

if true_one:
    print("This statement is true")
print("this statement will print no matter what")

# if else statements
# if (this is true)
# perform these actions
# else: OTHERWISE
# this will happen
# actions outside of indentations will happen no matter what
is_true = True

if is_true:
    print("this statment is true")
else:
    print ("this statement is false")
print("this statment will print no matter what")

# if else if
# if the first statement is false it will check the second conditional
x = 23
y = 32

if x > y:
    print(x, "is greater than", y)
elif x + y > 100:
    print(x + y, "is greater than", 100)
else:
    print("niether statement is true")

# Loops - a conditional that continues until a staement is false,m or the end is reached

# while loop - a condiditonal that continues until a statement is false
x = 0

while x < 10:
    print(x)
    x = x + 1
# this will print x and then add 1 to x until it gets to 9 and then it will stop

# DANGER OF LOOPS
# z = 0
# while z < 10:
    # # print(x)
    # y = x + 1
# this will cause an infinite loop and it will keep returning 0. IT DOES NOT STOP

# for loop - a conditional that contunes until the end is reached
number = [1,2,3,4]

for num in number: # num is going to be defined within the for loop, and auto increments through my list
    print(num)

for num  in range(1, 11): #range(x,y) --> x <= num <y - the number is going to be greater and or equal to x but it will be less than y
    print(num)