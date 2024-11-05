from loguru import logger
"""Password Guessing Game:
Create a password guessing game 
where the user has a limited number of attempts to guess 
the correct password. Use a while loop to continue prompting the user for
guesses until either they guess the correct password or they run out of attempts."""

# password = input("Enter the password")
# attempts = int(input("Enter the number of attempts"))
# def password_guessing_game(password, attempts):
#     attempted = 0
#     while(attempted < attempts):
#         attempted_password = input("Guess the password")
#         if(attempted_password == password):
#             logger.info("You guessed correct password")
#             break
#         else:
#             logger.info("Try again!!!")
#         attempted += 1
        
# password_guessing_game(password,attempts)


"""Number Guessing Game:
Develop a number guessing game where the computer generates a random number 
and the user tries to guess it. Use a while loop to keep the game 
running until the user either guesses the correct number or chooses to quit."""
# import random
# randomNumber = int(random.random()*10)
# logger.info(randomNumber)

# def number_guessing_game(randomNumber):
#     print("Enter q to end the game")
#     while(True):
#         inp = input("Enter input")
#         if(inp == "q"):
#             break
#         elif(int(inp) == randomNumber):
#             logger.info("You guessed correct number")
#             break
#         else:
#             logger.info("you guessed wrong number")
    
# number_guessing_game(randomNumber)

"""Factorial Calculation:
Write a Python program to calculate the factorial of a given number using a while loop.
"""
# num = int(input("Enter the number: "))

# if( num >= 0):
#     if(num==0):
#         logger.info(f"{num}! is 1")
#     elif(num == 1):
#         logger.info(f"{num} is 1")
#     else:    
#         def finding_factorial(num):
#             factorial = 1
#             i = num
#             while( i > 0):
#                 factorial = i * factorial
#                 i -= 1
#             logger.info(factorial)
#         finding_factorial(num)
# else:
#     logger.info("Enter the positive Number")
    
#Create a Python program to generate the 
# Fibonacci sequence up to a specified number of terms using a while loop.
# count = 1 
# first_number = 0
# second_number = 1
# next_number = second_number

# while(count < 11):
#     print(next_number ,end=" ")
#     count +=1
#     first_number = second_number
#     second_number = next_number
#     next_number = first_number +second_number

"""Write a Python program that continuously prompts the user to 
enter a number until they enter a negative number. Calculate and 
display the sum of all the positive numbers entered by the user."""
sum = 0
while(True):
 
    inp = int(input("Enter the number : "))
    if(inp < 0):
        break
    else:
        sum = sum + inp
    
logger.info(sum)

