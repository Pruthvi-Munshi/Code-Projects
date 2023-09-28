# Write a Python program that calculates the sum of all even numbers in a specified range [start, end],
# where start and end are integers provided by the user.

# need to identify the even number!!!!
# can you modular (%) to divde number by 2, if it returns 0 then it is even number

x = input("Enter the number 1: ")
y = input("enter the number 10: ")

# user_range = [x , y]

# print(user_range)

# # while loop - a condiditonal that continues until a statement is false
# x = 0

# while x < 10:
#     print(x)
#     x = x + 1
# # this will print x and then add 1 to x until it gets to 9 and then it will stop




# # for loop - a conditional that contunes until the end is reached
# number = [1,2,3,4]

# for num in number: # num is going to be defined within the for loop, and auto increments through my list
#     print(num)

# for num  in range(1, 11): #range(x,y) --> x <= num <y - the number is going to be greater and or equal to x but it will be less than y
#     print(num)

even_sum = 0

for even_num in range(int(x) , int(y)+1):
    if even_num % 2 == 0:
        even_sum = even_sum + even_num # can create variable in the for loop, do not need to be predefined but you should in here 
        # even_sum += num --> same as even_sum = even_sum + even_num
print(even_sum)