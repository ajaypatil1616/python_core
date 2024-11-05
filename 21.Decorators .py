#using decorators we can add features to existing functions with touching them

# def division(a,b):
#     print(a / b)

# def outer_function(arg_function):
    
#     def inner_function(a,b):
#         if (a < b):
#             a, b = b, a
#         return arg_function(a,b)
        
#     return inner_function


# division1 = outer_function(division)

# division1(2,4)


##
#2nd Example
# def my_decorator(original_func):
#     def wrapper():
#         print("DO a thing Before")

#         original_func()

#         print("Do a thing after")

#     return wrapper

# @my_decorator
# def greeting():
#     print("Hello Greeting")
    
# greeting()


##
# decorators allows to modify the behaviour of a function or class.
#In Python, functions are first class objects which means that 
#functions in Python can be used or passed as arguments.

# def decorator_function(actual_function):
    
#     def inner_wrapper_function():
#         print("Before actual function to be called")
#         actual_function()
#         print("after actual function is called")
#     return inner_wrapper_function

# def actual_function():
#     print("I am actual function")
    
# actual_function = decorator_function(actual_function)
# actual_function()


##
#Another example
import time,math

# def calculate_time (factorial_function):
#     def inner_wrapper_function(*args):
#         begin = time.time()
#         factorial_function(*args)
#         end = time.time()
#         print(f"Total time taken in : {factorial_function.__name__} is {end-begin}")
#     return inner_wrapper_function

# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))
    
# factorial(5)


##
# Chaining Decorators is used for Retry logging

# def first_decorator_function(func):
#     def inner_wrapper_function():
#         x = func()
#         return x * x
#     return inner_wrapper_function

# def second_decorator_function(func):
#     def inner_wrapper_function():
#         x = func()
#         return x * 2
#     return inner_wrapper_function

# @first_decorator_function
# @second_decorator_function
# def func():
#     return 5

# @second_decorator_function
# @first_decorator_function
# def func2 ():
#     return 20

# print(func()) #100
# print(func2()) #800


##
#static method in python does not needs object to call and is called on class
# @staticmethod #declaring static method
# import math
# class MathUtils:
#     @staticmethod
#     def factorial(number):
#         if (number == 0):
#             return 1
#         else:
#             return math.factorial(number)
# print(MathUtils.factorial(5))

#normal method is called with object created of that class
#static and class method(@classmethod) called with className.methodName


## there are 3 types of methods in python
#1.normal method
#2. @staticmethod
#3. @classmethod


# Decorators with inheritance and polymorphism
#this is custom decorators

# def uppercase(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper

# class BaseClass:
#     @uppercase
#     def greet(self):
#         return "Hello"

# class DerivedClass(BaseClass):
   
#     def __init__(self) -> None:
#         super().__init__()
#     @uppercase
#     def greet(self):
#         return "Hi"
    
    
# childObj =DerivedClass()
# print(childObj.greet())

# parent_obj = BaseClass()
# print(parent_obj.greet())