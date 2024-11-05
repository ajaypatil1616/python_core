from loguru import logger


#Q1 Write a function to remove duplicate elements from a list.
# def remove_duplicates_form_list(list_containing_duplicates):
#     new_list = set(list_containing_duplicates)
#     logger.info(list(new_list))

# remove_duplicates_form_list([1,1,1,1,1,1,12,2,2,2])


#Q2:  Implement a function to find the second largest element in a list.

# def finding_second_highest_element(ls):
#     ls.sort(reverse =True)
#     logger.info(ls[1])
# finding_second_highest_element([1,2,23,4,5,3,68,65,96,999])


#Q3: Write a program to reverse a list without using the built-in reverse() function.
# ls = [1,2,3,4,5,6,7,8,9,10]
# new_ls = []
# for i in range(len(ls)-1,-1,-1):
#     new_ls.append(ls[i])
# logger.info(new_ls)          


#Q4: Create a function to merge two sorted lists into a single sorted list.
# def merging_sorted_list (list1, list2):
#     list1.sort()
#     list2.sort()
#     list3 = list1 + list2
#     list3.sort()
#     logger.info(list3)
    
# merging_sorted_list([1,4,3,2,5],[11,105,6,7,9,8])

        
#Q5 . Implement a function to find the intersection of two lists.

# def intersection_of_list (list1, list2):
#     logger.info(list(set(list1).intersection(set(list2))))

# intersection_of_list([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9])

# intersection_list = []
# def intersection_of_lists(list1, list2):
#     for i in range(0,len(list1),1):
#         for j in range(0,len(list2),1):
#             if(list1[i] == list2[j]):
#                 intersection_list.append(list1[i])

# intersection_of_lists([1,2,3,4,5,6,7,1000,101],[1,2,101,3,4,5,6,7,8,9,1000])
# logger.info(intersection_list)


#TUPLE Questions
#Q1: Write a function to convert a tuple to a dictionary.
# def convert_tuple_to_dictionary(tuple):
#     logger.info(dict(tuple))
#     logger.info(type(dict(tuple)))
    
# convert_tuple_to_dictionary(((1,1),(2,2),(3,3)))


#Q2:  Write a program to unzip a list of tuples into separate lists
# new_list = []
# def unzip_tuples_from_list(list_of_tuples):
#     for a,b,c in list_of_tuples:
#         new_list.append(a)
#         new_list.append(b)
#         new_list.append(c)
# unzip_tuples_from_list([(1,2,3),("ajay","akshay","supriya"),(55,45,95)])
# print(new_list)


#Q3 :Create a function to check if a given element exists in a tuple.
# def finding_element_in_tuple(element,tuples):
#     for x in tuples:
#         if(x == element):
#             print(f"{element} is present in this tuple")
        
# finding_element_in_tuple(10,(1,2,3,45,6,10))
# print(10 in (1,2,3,45,6,10))
# print(10 not in (1,2,3,45,6,10))


#Q4:Implement a function to calculate the dot product of two tuples.

a_of_tuples = []
b_of_tuples = []
def calculating_dot_product(tuples):
    for a,b in list(tuples):
        a_of_tuples.append(a)
        b_of_tuples.append(b)
    dot_product = a_of_tuples[0] * b_of_tuples[0] + a_of_tuples[1] * b_of_tuples[1]
    print(dot_product)
        
calculating_dot_product(((1,2),(3,4)))
