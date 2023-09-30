# Function - is like a mini program within a program
# print(), len(), input() all examples of function

# creat function called hello

def hello():
    print("Howdy!") #must have something in fucntion

# call a function
hello()

#valu that you pass to a funtion is called an argument
# creat function that has a parameter

# # cannot have two funtions with same name
# def hello2(name): # (name) is a variable, and this variable name we call a parameter
#     print("Hi, " name)
# # #PARAMETER - variable name that represent an argument that needes to be passed

# hello2("Syco") #"syco" here is an arguement
# my_name = "Kay"
# #ARGUEMENT - represents the data that is passed to the function

# hello(my_name) #

#my_name should not be used inside the funtion 
#YOU ASSIGN THE ARGUEMENT TO THE PARAMETER

#purpose of fucktion is to make job easy code clean but most of time we need return value but print does not do that
#instead we will use return

import random #import staement is used to include external modules or libraries in your code
#this can include fucntions, classes, and variables

def get_fortune(random_num):
    if random_num == 1:
        return "it is likely"
    elif random_num == 2:
        return "answer unknown"
    elif random_num == 3:
        return "def not"
    
num = random.randint(1, 3) #in there random is the object from the import library
#randint is a method, kinda like a function that gives random value, like a funtion but not the same

print(get_fortune(num))

#or

my_fortune = get_fortune(num) #retun lets completion of a funtion assign a value
print(my_fortune)

#fucntion can have multiple parameters
def add(num_one, num_two): #multiple parameter, can be unlimited but must have the same amount of arguments as paramtere
    return num_one + num_two

print (add(6, 9)) #returns and saves the number 

# note that the standalone function() is a function, not to be confused with a method...
# a method is a call made alongside an object (we'll go more into objects later) some methods we have seen before:
# .add(), .append(), .index(), etc. notice the ".", because methods will always be attached to a variable/obj

#FUNCTION PRACTICE
#creater a function that takes two numbers and calculates num1^num2 (num1 to the power of num2)

#take num1 and get num1 to multiply by itself to the amount of num2
# first get num1 and get it to multiply by itself

#power of:
#step one is to mutiply num1 * num1
#step two multiply num1

#multiply num1 * num1 save the value and add one to the counter
# then get the saved value and multiply by num1

def power(num1, num2):
    num1_mult = num1
    num2_count = 2
    while num2_count <= num2:
        num2_count = num2_count + 1
        num1_mult = num1_mult * num1
        print("num count:", num2_count)
        print("num multiply, current value:", num1_mult)
    return (num1_mult)

print(power(12, 7))

print(12**7)
    
# factoprial problem - create a function that creates a afactorial of a number 
# ex: factorial(5) -> ouput 5! = 120 (5x4x3x2x1)
# get num1 to multiply num1-1 until it hits one cannot go to 0
#do not tamper with num1

def fact1(num1):
    ret_val = 1
    # mult_val = num1*ret_val
    num_sub = num1
    while num_sub >= 1:
        ret_val = ret_val * num_sub
        num_sub = num_sub - 1
        print("num sub count:", num_sub)
        print("ret value: ", ret_val)
    return (ret_val)

print(fact1(4))