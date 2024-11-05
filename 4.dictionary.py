from loguru import logger

#Dictionary : stores in key value pair (JSON)
# dictionary is ordered, changeable and do not allow duplicates(key)
#dictionary can not have two items with the same key

my_dict = {
    "name":"ajay",
    "age": 25,
    "city": "KOP",
    "birth_year": 2000
}
# logger.info(my_dict)

# logger.info(my_dict["name"])
# logger.info(my_dict["age"])
# logger.info(my_dict["birth_year"])

# logger.info(len(my_dict))
# logger.info(type(my_dict))

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

#get("key")
# logger.info(my_dict.get("age"))

# logger.info(my_dict.keys())
# logger.info(my_dict.values())

# add new 
my_dict["domain"] = "PySpark"
# logger.info(my_dict)

#items()
# logger.info(my_dict.items())

#cheking key is present or not
# if "age" in my_dict:
#     logger.info("age is present in dictionary")

#change value in dictionary 
my_dict["age"] = 28
# logger.info(my_dict)

#update() 
my_dict.update({"birth_year":1997})
# logger.info(my_dict)

#adding using update()
my_dict.update({"company":"dynamisch"})
# logger.info(my_dict)

#pop("key")
# my_dict.pop("company")
# logger.info(my_dict)

#popitem() :removes last inserted item
# my_dict.popitem()
# logger.info(my_dict)

#del : used to delete the whole dictionary
# del my_dict
# logger.info(my_dict)

#looping inside dict 
# for x in my_dict:
#     logger.info(x)#prints only keys
    
# for x in my_dict.values():
#     logger.info(x) # prints the values here
    
# for x,y in my_dict.items():
#     print(x, y)

#copy dict
new_dict = my_dict.copy()
# logger.info(new_dict)

#Nested dictionary
myFamily = {
    "child1":{
        "name":"Akshay",
        "age": 28,
        "salary":20000
    },
    "child2":{
        "name":"supriya",
        "age": 27,
        "salary": 15000
    },
    "child3":{
        "name": "ajay",
        "age": 25 ,
        "salary": 16000
    }
}

logger.info(myFamily["child3"]["name"])
logger.info(myFamily["child2"]["salary"])