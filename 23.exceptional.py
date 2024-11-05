# what is 
# how is 
## where to use  

#1. File handling
#finally : is used in file handling closing file  f.close()
#2.Input Validation:
#3.Database Operations : connection failure,
#4.Arithmetic Operations : division by zero
#5. API call


# mainly two types errors 
#1. syntax error / Parsing error
#2. exceptions : errors detected during execution(runtime) are called execptions 

# print(10 * 1/0)
# print(4 + spam*3)
# print("1"+1)

#try : lets you test a block of code for errors
#except : handles the error
#else : when there is no error else is executed
#finally : It will be executed at any cost(regardless the result of try - except blocks)

# print(x)
# try:
#     print(x)
# except:
#     print("An error Occured")
    
    
# try:
#     print(x)
# except NameError :
#     print("Variable x is not defined")
# except:
#     print("something else went wrong")
    
    
# try:
#     print("Hello")
# except:
#     print("some error")
# else:
#     print("This is executed because there is no error in try block")


# try:
#     print("Try block will find any error occured or not")
# except:
#     print("Except block will executed when there is an error")
# else:
#     print("Else block will run when there is no error")
# finally:
#     print("Finally will run regardless of anything happened above")

 
# try:
#     f = open("exception.txt","x")
#     try:
#         f = open("exception.txt","w")
#         f.write("Hi My name is python")
#     except:
#         print("an error occured while writing")
#     finally:
#         f.close()
# except:
#     print("error occured while creating file")


##
# As a developer you can throw/raise an exception when some specific condition met/occurs
#You can define what kind of error to raise
# we can create error using raise

# x = -1
# if x < 0:
#     raise Exception("Number can not be less than 0")


# y = "Hello"

# if not type(y) is int :
#     raise TypeError("Only integers allowed")
# # print("Hi")
##
def myfunction():
    x = 10/0

# try:
#     myfunction()
# except ZeroDivisionError as e:
#     print(e)
# except :
#     print("Normal error")


#All types of exception
"""
SyntaxError: Raised when there is a syntax error in the code.

IndentationError: Raised when there is incorrect indentation.

NameError: Raised when a local or global name is not found.

TypeError: Raised when an operation or function is applied to an object of inappropriate type.

ValueError: Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

ZeroDivisionError: Raised when the second operand of a division or modulo operation is zero.

IndexError: Raised when a sequence subscript is out of range.

KeyError: Raised when a dictionary key is not found.

FileNotFoundError: Raised when a file or directory is requested but cannot be found.

IOError: Raised when an input/output operation fails.

EOFError: Raised when there is no input from the user (End Of File).

AttributeError: Raised when attribute reference or assignment fails.

ImportError: Raised when the import statement fails to find the module definition.

ModuleNotFoundError: A subclass of ImportError raised by import when a module could not be found.

PermissionError: Raised when trying to access a file or resource without appropriate permissions.

RuntimeError: Raised when a generated error does not fall into any category.

KeyboardInterrupt: Raised when the user hits the interrupt key (Ctrl+C or Delete).

AssertionError: Raised when an assert statement fails.

ArithmeticError: Base class for arithmetic errors.

MemoryError: Raised when an operation runs out of memory."""