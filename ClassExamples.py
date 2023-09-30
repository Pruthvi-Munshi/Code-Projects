#a class is blueprint of creating objects
# basic syntax for defining a class in python

# bit diff class names use camel case
class ClassName:
    # class variables are shared by all instances on a class
    class_var = "i am a class variable"

# every class has a constructor - constructor is properties that you object is going to hold
    def __init__(self, parameter1, parameter2):
        self.instance_variable1 = parameter1 #instance variable 1
        self.instance_variable2 = parameter2 # instance var 2

# when your object in here it is the classname
# constructor method assigns parameters to the object

# instance method can access and modify instance variables
    def instance_method(self):
    # do something w/ instance variables
        print("i am an instance method")
        print("instantce var 1: ", self.instance_variable1)
        print("instance var 2: ", self.instance_variable2)

# calling a class == object creations
# we are creating an instance of the class
obj_name = ClassName("value1", "value2")

# can acess a class variable 
print(ClassName.class_var)

# call instance method
obj_name.instance_method()

# class example
# Class animal
class Animal:
    # calss var
    animal_type = "Unkown"

    def __init__(self, name, sound): #constructor is defining the properties
        # instance var
        self.name = name
        self.sound = sound
    
    # isntacne method to make animal sound
    def make_sound(self): # instace method is the behaviour
        print(f"The {self.animal_type} name {self.name} make the sound {self.sound}")

#  create two instances

lion = Animal("Lian", "Rawr")
dog = Animal("Dog", "Bark")

# access class var
print("Animal type:", Animal.animal_type)

# calling instance methods
lion.make_sound()
dog.make_sound()

# class example -> person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello my name is {self.name} and i am {self.age}")

adam = Person("Adam", "30")
skye = Person("Skye", "30")

adam.greet()
skye.greet()

# can also call specfic atributes
print(adam.age)

# abstraction is a fundamental principle of object-oriented design. 
# It allows programmers to create a blueprint for objects
# A class is an abstraction of real-world entities, defining their properties (attributes) and behaviors (methods).

# constructor is defining the properties
# instace method is the behaviour

# calss example ->
class BankAccount:
    def __init__(self, acc_num, balance=0):
        self.acc_num = acc_num
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Depostited ${amount}. New balance: ${self.balance}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw ${amount}. New Balance: ${self.balance}")
        else:
            print("Youre too broke")

# example for usage
account1 = BankAccount("001")
account1.deposit(1000)
print(account1.balance)

account1.withdraw(500)
account1.withdraw(1000)