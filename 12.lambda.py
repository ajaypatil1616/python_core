#Lambda Function (anonymous = hidden)
#It is an anonymous function that takes any number of arguments but can have only one expression

# x = lambda a,b,c : a+b+c
# print(x(10,10,10))
# print(type(x))

#Real power of lambda comes in picture when we use it inside another function

#Filtering Even Numbers:
#Write a lambda function to filter even numbers from a list of integers.

# ls = [1,2,3,4,5,6,7,8,9]
# op = map(lambda x: x % 2 == 0 ,ls)
# print(list(op))


#Calculating the Square of a Number:
# Write a lambda function to calculate the square of a given number.

# ls = [1,2,3,4,5,6,7,8,9]
# x = map(lambda x: x**2, ls)
# print(list(x))


#Even odd find from list  

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = []
# odd_numbers = []
# list(map(lambda x : even_numbers.append(x) if x % 2 == 0 else odd_numbers.append(x),numbers))
# print(even_numbers)
# print(odd_numbers)

#  square of this list
# numbers = [1,2,3,4,5,6,7,8,9,10]
# square_of_numbers = map(lambda x : x**2 ,numbers)
# print(list(square_of_numbers))

# Sorting
# tuples = [ (1, 5), (2, 3), (3, 8), (4, 1)]
# Output: [(4, 1), (2, 3), (1, 5), (3, 8)]


# tuples = [(1, 5), (2, 3), (3, 8), (4, 1)]

# for i in range(len(tuples)):
#     for a,b in tuples[i]:
#         if()


#MAP:map(function, sequence) executes specified function for each item in sequence
"""You have a list of lists containing numbers. 
Write a lambda function to square each number and then flatten the list."""

# ls = [(1,2,3),(4,5,6),(7,8,9)]
# new_ls = []
# for a,b,c in ls:
#     new_ls.append(a)
#     new_ls.append(b)
#     new_ls.append(c)
# print(new_ls)
# x = lambda x : x ** 2
# print(list(map(x,new_ls)))