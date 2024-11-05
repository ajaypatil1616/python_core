from loguru import logger
#Tuple : tuple are immutable(can not be changed), ordered(definite order) and allow duplicates
# tuples can store any kinds of data

my_tuple = ("vinay","Ajay","Prasad","Nikita","pooja","supriya","AKshay")

#len
# logger.info(len(my_tuple))
# logger.info(type(my_tuple))
# logger.info(tuple([1,2,3,4,5,69]))# converts list to tuple

#Accesing tuple using indexing OR slicing
# logger.info(my_tuple[::-1])
# logger.info(my_tuple[1:6:4])
# logger.info(my_tuple[-7 : -3:1])

#check if item exists 
# if "supriya" in my_tuple :
#     logger.info("True")

# Tuples are immutable means that they can not be change, add, remove items
# If you wanna change tuple then convert it into list and then change  and again convert it to the tuple

#If u wanna add, remove or change any element in tuple then convert it to list......
# changeable_tuple = (1,2,34,5,6)
# x = list(changeable_tuple)
# x[2]="Ajay"
# changeable_tuple = tuple(x)
# logger.info(changeable_tuple)

#del : completely delete the tuple
# del my_tuple
# logger.info(my_tuple) # this will give an error because you deleted the tuple


#Unpacking of tuple
    
#eg.1

# packing_tuple = ("red","blue","gray")
# (ajay,supriya,akshay) = packing_tuple
# logger.info(ajay)
# logger.info(supriya)
# logger.info(akshay)


#eg.2 with astericks

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (red, *yellow, green) = fruits # here * represents all remaining parameters except for red
# logger.info(red)
# logger.info(yellow)
# logger.info(green)
# logger.info(type(yellow)) # its list

#Looping through a tuple

# for x in my_tuple:
#     logger.info(x)
    
# for i in range(0,len(my_tuple),1):
#     logger.info(my_tuple[i])
    
# i = 0 
# while ( i < len(my_tuple)):
#     logger.info(my_tuple[i])
#     i += 1

#join the tuple
# joining_tuple = (1,2,34,6,69)
# joined_tuple = my_tuple + joining_tuple
# logger.info(joined_tuple )

# multiplied_tuple = my_tuple * 2
# logger.info(multiplied_tuple)

#count(value)
# logger.info(my_tuple.count("Ajay"))

#index(value)
# logger.info(my_tuple.index("AKshay"))