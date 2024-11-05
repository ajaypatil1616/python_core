#A class is like object constructor or a  blueprint for object

class Class_example :
    x = 10

obj = Class_example()
# print(obj.x)

# __init__() 
# All classes have __init__() function(constructor) which always executed when a class is being initiated.
### __init__() is used to assgin values to object properties
#The __init__ ( ) allows you to initialize the attributes (variables) of an object.
#The __init__() function is called automatically every time the class is being used to create a new object.

class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age
       
person1 = Person("Ajay",25)
person2 = Person("Akshay",24)
# print(person1)
# print(person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)

#self allows the __init__ method to access the object's attributes and methods.
#self refers to the object

#__str__()
# __str__() controls what should be returned when class object is represented as  string
# If the __str__() is not  set then string representation of object is returned

# class PERSON:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def __str__(self) :
#         return f"{self.age} {self.name}"

# ajay = PERSON("AJAY",25)
# print(ajay)

class Railway:
    def __init__(self, name, age, date, payment):
        self.name = name
        self.age = age
        self.date = date 
        self.payment = payment
    def registration(self):
        print(f"{self.name} your age is {self.age} and\
            your registration of the date {self.date} is confirmed {self.payment} ")
    
railway_ajay = Railway("ajay",25,"16-03-200",True)
railway_ajay.age = 49

#deleting age property from object 
#del railway_ajay.age

railway_ajay.registration()
Railway.registration(railway_ajay)

#The self parameter is a reference to the current instance of the class, and is used to 
#access variables that belongs to the class.