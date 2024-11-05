#Polymorphism :The Word Polymorphism means having many forms.
#A object behave differntly in different situations
#Same function name being used for different purposes

# Inbuilt polymorphic function
# print(len("ajay"))
# print(len(["1",2,3,5,6,8,10]))


#user defined polymorphic function
# def add(x,y,z =0):
#     return x+y+z

# print(add(10,10))
# print(add(10,10,10))

#Polymorphism with class methods

# class India:
#     def capital(self):
#         print("New Delhi")
#     def lang(self):
#         print("Hindi")
#     def type(self):
#         print("developing country")

# class USA:
#     def capital(self):
#         print("Washington DC")
#     def lang(self):
#         print("English")
#     def type(self):
#         print("developed country")

# india_object = India()
# usa_object = USA()

# for country in (india_object, usa_object):
#     country.capital()
#     country.lang()
#     country.type()


#Polymorphism with Inheritance
class Employee:
    def __init__(self,name, id) -> None:
        self.id = id
        self.name = name
    
    def calculate_salary(self):
        print("Salary from Base Employee")
    
    def display_info(self):
        print(f"name: {self.name} with id {self.id}")

class FullTimeEmployee(Employee):
    def __init__(self, name, id,salary) -> None:
        super().__init__(name, id)
        self.salary = salary
    def calculate_salary(self):
        print(f"salary from full time Emloyee {self.salary}")
    def display_info(self):
        print(f"name : {self.name} , id : {self.id}, salary : {self.salary}")
        
class PartTimeEmployee(Employee):
    def __init__(self, name, id,hourly_rate,total_hours_work) -> None:
        super().__init__(name, id)
        self.hourly_rate =hourly_rate
        self.total_hours_work = total_hours_work
    def calculate_salary(self):
        print(f"salary {self.hourly_rate * self.total_hours_work}")
    def display_info(self):
        print(f"name : {self.name} , id : {self.id}, salary : {self.hourly_rate * self.total_hours_work}")
        

employee_obj_list = [
   FullTimeEmployee("Ajay",81,16004),
   PartTimeEmployee("Vivek",24,700,8),
]
for emp in employee_obj_list:
    emp.calculate_salary()
    emp.display_info()