from loguru import logger

#Set : sets are unorderd(unindexed), unchangeable(we can add/remove items but can't change)
#sets do not allows duplicates
#Value of True and 1 in sets are same 
#Value of Flase and 0 in sets are same 
# sets = {True, 1,1, False, 00,0,0}
# logger.info(sets)

my_sets = {"dimple","aditya","rohit","aditi","ajay"}

# logger.info(len(my_sets))
# logger.info(type(my_sets))
# logger.info(set([1,2,2,2,2,2,1,2,2,211]))

# for x in my_sets:
#     logger.info(x)

# logger.info("ajay" in my_sets) # prints True
# logger.info("dimple" not in my_sets)

# add()
# my_sets.add("ramesh")
# logger.info(my_sets)

# update(): To add items from another set into current set is using update()
# new_set = {1,2,3,4,5}
# my_sets.update(new_set)
# logger.info(my_sets)

#remove():If the item to remove does not exist, remove() will raise an error.
# my_sets.remove("ajay")
# logger.info(my_sets)
#discard :If the item to remove does not exist, discard() will NOT raise an error.
# my_sets.discard("ramesh")
# logger.info(my_sets)

#clear : clears the all the set
# my_sets.clear()
# logger.info(my_sets)

# del :deletes the set
# del my_sets
# logger.info(my_sets)

#looping the set
# for x in my_sets:
#     logger.info(x)

#JOIN sets
#1.union/update
#update(): does not return new set, it alters existing set
#union(): returns new set after the joining
new_set = {1,2,3,4,5,6,7}
set4 = {"SDF","Sfd",4}
set3  = my_sets.union(new_set,set4)
logger.info(set3)

#2.intersection(): retrun a new set
# intersection_update() : alters the existing set 
set5 = new_set.intersection(set4)
logger.info(set5)

#3.difference() : method will return a new set that will contain only the items from the first set that are not present in the other set.
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
c= a.difference(b)
logger.info(c)

