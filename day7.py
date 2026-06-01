#OOPS CONCEPT
#Example
# # example
# class Lakshya:
#   def __init__(self,name):
#     self.name = name
#   def show(self):
#     print(self.name)
 
# r = Lakshya("hello")
# r.show()

#EX1

# class Lakshya:
#   def __init__(self):
#     print("calling constructor")

#   def show(self):
#     print("show the name:")

# r = Lakshya()
# r.show()
      

# example 2

# class Lakshya:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def getAge(self):
#         print("My age is:", self.age)

#     def getName(self):
#         print("My name is:", self.name)

# r = Lakshya("hello", 20)

# r.getAge()
# r.getName()

#
## r = Lakshya(age=20,name ="hello")

## r.getAge()
## r.getName()

#Example3
# class student:
#     def __init__(self,*args):
#         print(type(args))
#         print(args)
    
#         self.name = args[0]

#     def getStu(self):
#         #print("the student is:",self.name)
#         return self.name

# s=student("hello",20,"0000000","arya@gmail.com")
# t=s.getStu
# print(t)



# example 4

# class student:
#     def __init__(self, *args):
#         self.data = args

#     def users(self):
#         print("The students are:", self.data[0])

#     def details(self):
#         print("Address is:", self.data[1]["address"])
#         print("College is:", self.data[1]["college"])


# s = student(
#     ["lakshya", "harshal", "harsh", "praveen"],
#     {"address": "kukas", "college": "arya"}
# )

# s.users()
# s.details()

