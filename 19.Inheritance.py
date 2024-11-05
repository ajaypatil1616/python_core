#Inheritance is simply inheriting variables and functions from parent  class
# parent class = base class
# child class = derived class

# class Person:
#     def __init__(self,first_name, last_name):
#         self.fname = first_name
#         self.lname = last_name
#     def print_name (self):
#         print(f"{self.fname} {self.lname}")

# x = Person("aditya","datte")
# x.print_name()

#To create child class, send parent class as an argument to the child class
#when we create __init__() in child class it overrides the inheritance of parent class __init__()
# class Student(Person):
#     def __init__(self, first_name, last_name,year):
#         super().__init__(first_name, last_name)
#         self.graduation_year = year
        
#     def welcome(self):
#         print(f"{self.fname} {self.lname} welcome you from the graduction year {self.graduation_year}")


# y = Student("Mike","Hisen", 2022)
# y.print_name()
# y.welcome()

#super() function that will make the child class inherit all the methods and properties from its parent



##
# Types of inheritance :Types of Inheritance depend upon the number of child and parent classes involved
#1. Single Inheritance 
# a situation where a derived class inherits from a single base class

# class Nokia :
#     def __init__(self):
#         pass
    
#     company = "Nokia India"
#     website = "www.nokiaindia.com"

#     def contact_details(self):
#         print(f"Address : 1408 B ward, Mangalwar Peth, Kolhapur")

# class NokiaC201(Nokia):
#     def __init__(self):
#         self.name = "Nokia C2-01"
#         self.year = 2012
        
#     def product_details(self):
#         print(f"Name : {self.name}")
#         print(f"year : {self.year}")
#         print(f"company: {self.company}")
#         print(f"website: {self.website}")

# mobile = NokiaC201()
# mobile.contact_details()
# mobile.product_details()


#2.Multiple inheritance
#When a class is derived from more than on base class is called multiple inheritance
# class Father:
#     father = ""
#     def father_name(self):
#         print(self.father)

# class Mother:
#     mother = ""
#     def mother_name(self):
#         print(self.mother_name)

# class Child(Father, Mother):
#     def print_parent_names(self):
#         print(f"Mother's Name {self.mother}")
#         print(f"Faters's Name {self.father}")
        

# child = Child()
# child.father = "Balasaheb"
# child.mother = "Savita"


# child.print_parent_names()


#3. Multilevel Inheritance
# In multilevel inheritance  class is dervired from intermediate 
# class which will be derived from base class


# class Grandfather:
# 	def __init__(self, grandfathername):
# 		self.grandfathername = grandfathername


# class Father(Grandfather):
# 	def __init__(self, fathername, grandfathername):
# 		self.fathername = fathername		
# 		Grandfather.__init__(self, grandfathername)

# class Son(Father):
# 	def __init__(self, sonname, fathername, grandfathername):
# 		self.sonname = sonname	
# 		Father.__init__(self, fathername, grandfathername)

# 	def print_name(self):
# 		print('Grandfather name :', self.grandfathername)
# 		print("Father name :", self.fathername)
# 		print("Son name :", self.sonname)



# s1 = Son('Ajay', 'Balasaheb', 'Dnyndev')

# s1.print_name()



#4.Hierarchical Inheritane
#When more than one derived class are created from single Base class is called Hierarchical Inheritance
 
# class Parent:
#     def parent_fun(self):
#         print("This is from parent class")

# class Child1(Parent):
#     def child1_fun(self):
#         print("THis is from child1 class")

# class Child2(Parent):
#     def child2_fun(self):
#         print("This is from child2 class")

# obj1 = Child1()
# obj2 = Child2()

# obj1.child1_fun()
# obj1.parent_fun()

# obj2.child2_fun()
# obj2.parent_fun()



#5.Hybird Inheritance
#Inheritance consisting of multiple types of inheritance is called hybrid inheritance

class School:
    def func1(self):
        print("THis is from Base School")

class Student1(School):
    def func2(self):
        print("This is from Student1 ")

class Student2(School) :
    def func3(self):
        print("THis is from Student 2 ")
    
class Student3(Student1,School):
    def func4(self):
        print("This is from the student 4")
    
obj = Student3()
obj.func4()
obj.func1()
obj.func2()
