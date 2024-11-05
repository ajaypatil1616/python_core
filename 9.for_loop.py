# Printing Patterns:
# Write a Python program to print the following patterns using nested for loops:

# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1,6,1):
#     for j in range(1,i+1,1):
#         print("*", end=" ")
#     print(" ")

# for i in range(1,6,1):
#     for j in range(1,i+1,1):
#         print(j, end= " ")
#     print(" ")


"""Multiplication Table:
Develop a Python program to generate the multiplication table (up to 10)
for a given number using a for loop."""


# for i in range(1,11,1):
#     for j in range(1,11,1):
        
#         print(i * j , end=" ")
     
        
#     print(" ")
   
"""List Comprehension:
Write a Python program that uses list comprehension to create a 
new list containing squares of numbers from 1 to 10."""
# x = [x**2 for x in range(1,11,1)]
# print(x)


"""Counting Characters:
Create a Python program that takes a string as input and counts the occurrences 
of each character using a for loop."""
# def counting_characters(string):
#     for x in string:
#         print(f"{x} is occured {string.count(x)}")
    
    
# counting_characters("ajay") 

"""Finding Prime Numbers:
Develop a Python program to find and print all prime numbers between 1 and 100 
using a for loop."""


#count the number of "the" in para
counter = 0
para ="The keyword is the most the The important word or phrase in a paragraph. It is the word that the paragraph is about, and it is the word that the reader should be able to identify after reading the paragraph. The keyword is usually placed in the topic sentence, which is the first sentence of the paragraph. The keyword is also often repeated throughout the paragraph, and it is often emphasized in some way, such as by being italicized or bolded."
para = para.split(" ")
para = list(para)
for i in range(len(para)):
    if (para[i] == "the"):
        counter += 1
    
print(counter)
    



"""

*****
***
*
*
***
*****

"""

# for i in range(3):
#     print("* " * (5-i))

        