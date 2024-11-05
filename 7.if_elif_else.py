from loguru import logger
# """Grade Classification:
# Write a Python program that takes a student's score as input and classifies their grade as 'A', 'B', 'C', 'D', or 'F' based on the following criteria:

# A: 90 - 100
# B: 80 - 89
# C: 70 - 79
# D: 60 - 69
# F: Below 60 """


# def student_grade(score):
#     grade = ""
#     if(score == 100):
#         grade = "A++"
#     elif(score >=90 and score <100):
#         grade = "A"
#     elif(score >=80 and score < 90):
#         grade = "B"
#     elif (score >=70 and score < 80) :
#         grade = "C"
#     elif (score >=60 and score <70):
#         grade = "D"
#     else:
#         grade="F"
        
#     logger.info(grade)
        
# student_grade(78)


"""Leap Year Checker:
Develop a Python program that determines whether a given year is 
a leap year or not. A leap year is evenly
divisible by 4, but not by 100 unless it is also divisible by 400."""

# def leap_year_determination(year):
#     if(year % 400 ==  0 and year % 4 == 0 and year % 100 == 0 ) :
#         logger.info(f"{year} is leap year")
#     elif(year % 4 == 0 and year % 100 != 0):
#         logger.info(f"{year} is leap year")
#     else:
#         logger.info(f"{year} is not leap year")
        
# leap_year_determination(2004)

"""BMI Calculator with Classification:
Create a Python program that calculates Body Mass Index (BMI) based on user
input of height (in meters) and weight (in kilograms).
Classify the BMI according to the following categories:
Underweight: BMI < 18.5
Normal weight: 18.5 <= BMI < 25
Overweight: 25 <= BMI < 30
Obesity: BMI >= 30"""

# def calculate_BMI(weight,height):
#     BMI = weight / height * height
#     if(BMI < 18.5):
#         logger.info("Underweight")
#     elif(18.5 < BMI < 25):
#         logger.info("Normal weight")
#     elif( 25 <= BMI < 30):
#         logger.info("Overweight")
#     elif( BMI >= 30):
#         logger.info("Obesity")
#     else:
#         logger.info(f"your BMI is {BMI}")

# calculate_BMI(68,1.72)


"""Temperature Converter:
Design a Python program that converts temperature between Celsius and 
Fahrenheit based on user input. The program should 
prompt the user to choose the conversion direction and 
then perform the conversion accordingly."""

# conversion_type = int(input("press 1 for converting C to  F and Press 2 to convert F to C"))

# if(conversion_type == 1):
#     temp_in_celecius = float(input("Enter temp in celcuis: "))
#     temp_in_F = (9/5 *temp_in_celecius) + 32
#     logger.info(f"{temp_in_F} is temp in Faranite ")
# else:
#     temp_in_F = float(input("Enter the temp in Fara :"))
#     temp_in_celecius = (5/9)*(temp_in_F-32)
#     logger.info(f"{temp_in_celecius} is temp in celcuis ")


"""
Number Comparison:
Write a Python program that takes two numbers as input and 
determines which number is greater, or if they are equal. Provide appropriate 
messages based on the comparison results using if, elif, and else statements."""
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
def number_comparsion(num1,num2):
    if(num1 > num2):
        logger.info(f"{num1} is greater than {num2}")
    elif(num2 == num1 ):
        logger.info(f"{num1} and {num2} are equal")
    else:
        logger.info(f"{num1} is less than {num2}")
number_comparsion(num1,num2)

