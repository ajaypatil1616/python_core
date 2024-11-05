from loguru import logger
#List : Lists are ordered(definite order), changeable(mutable) and allow duplicates
#It can contains different kind of data types

#len()
my_list = ["zzz","apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#logger.info(f"{len(my_list)}")

#type()
# logger.info(f"{type(my_list)}")

#list() :typecast to list OR converts anything to list
thislist = list(("ajay","akshay","supriya"))
# logger.info(f"{thislist}")

#indexing
# logger.info(f"{my_list[-1]}")
# logger.info(f"{my_list[2]}")
# logger.info(f"{my_list[1:2]}")
# logger.info(f"{my_list[-4:-1]}")
# logger.info(f"{my_list[1:4:1]}")

#checking item is existing
# if "apple" in my_list:
    # logger.info(f"Apple is present in my_list")

#changing list items 
# my_list[2] ="ajay"
# logger.info(my_list)


#Changing a range in of item values
# my_list[1:4]= ["ajay","akshay","supriya"]
# logger.info(my_list)

#insert(index, value)
# my_list.insert(5,"dimple")
# logger.info(my_list)

#append()
# my_list.append("rohit")
# logger.info(my_list)

#extends
# extend_list = ["viraj", 'niraj']
# my_list.extend(extend_list)
# logger.info(my_list)

#We can extend our list with tuple/set/ dictonary
# extend_tuple = ("vinay","prasad")
# my_list.extend(extend_tuple)
# logger.info(my_list)

#remove(value)
# my_list.remove("banana")
# logger.info(my_list)

#pop(index): If you do not specify the index in  pop it will remove last element
# my_list.pop(5)
# logger.info(my_list)

#del
# del my_list[0]
# logger.info(my_list)

#clear() : clears all the elements of list
# my_list.clear()
# logger.info(my_list)

#looping a list 
# for x in my_list:
#     logger.info(x)
    
# for i in range(0,len(my_list),1):
#     logger.info(my_list[i])

# i=0
# while( i < len(my_list)):   
#     logger.info(my_list[i])
#     i +=1

#list comprehension
# [logger.info(x) for x in my_list]

#List comprehension :
# It is creating new list using existing list 

#1. Normal Approach
# new_list = []
# for x in my_list:
#     if "a" in x :
#         new_list.append(x)
# logger.info(new_list)

# #2. LC apporch
# new_list_using_LC = [x for x in my_list if "a" in x]
# logger.info(new_list_using_LC)

# new_LC = [x for x in range (1,101,1) if x % 2 == 0]
# logger.info(new_LC)

# new_list = [x.upper() for x in my_list]
# logger.info(new_list)

#sort
# my_list.sort()
# logger.info(my_list)

# my_list.sort(reverse= True)
# logger.info(my_list)

# numbered_list = [1,2,3,4,5,6,7,8,9,10]
# def sorted_function (n):
#     return n > 5
# numbered_list.sort(key=sorted_function)
# logger.info(numbered_list)

#case insensitive sort
# my_list.sort(key=str.lower)
# logger.info(my_list)

#reverse
# my_list.reverse()
# logger.info(my_list)

#copy()
# new_list = my_list.copy()
# logger.info(new_list)

#we can use this simple presence of  mind to copy of list
# new_list = list(my_list)
# logger.info(new_list)

#Join  two list  OR we can use extend()
# new_list = [1,2,3,4,565,5]
# joined_list = my_list + new_list
# logger.info(joined_list)

#count() : 	Returns the number of elements with the specified value
# logger.info(my_list.count("apple"))

#index : returns the index of first element with specified value
# logger.info(my_list.index("zzz"))

#Slicing
# Lst = [50, 70, 30, 20, 90, 10, 50]
# logger.info(Lst[::2])