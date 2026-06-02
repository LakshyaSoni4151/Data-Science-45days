# #CONSTRUCTOR
# class address:
#     # city ="jaipur"
#     # state="rajasthan"
#     def __init__(self,city,state): #this -> self
#         self.city = city
#         self.state = state
# a=address("jaipur","rajasthan")
# print(a.city)
# print(a.state)

# class Address:
#     def __init__(self,city,state):
#          self.city = city
#          self.state = state

#     def show(self):
#          print("the city is:",self.city)

# a=Address("jaipur","rajasthan")
# a.show()

# class Address:
#     def __init__ (self,city,state):
#         self.city=city
#         self.state=state

#     def location(self):
#         return f"my location is {self.city} in {self.state}"

# class User(Address):
#     def __init__(self,name,age,city,state):
#         super(). __init__(city,state)
#         self.name=name
#         self.age =age 
#         # self.city=city
#         # self.state =state

#     def Username(self):
#         print(f"my name is {self.name}")

#     def UserDetails(self):
#         print(f"my name is {self.name} and my location is {self.city} in {self.state}")



# u =User("rajendra",20,"kukas","rajasthan")
# print(u.city)
# u.UserDetails()

# u.location

#a = Address("kukas","rajasthan")

# #ENCAPSULATION
# class Address:
#   def __init__(self,city,state):
#     self.__city = city # private attribute
#     self.state = state
  
#   def location(self):
#     print(f"my location is {self.__city} in {self.state}")
 
#   def getcity(self):
#     return self.__city
 
# a = Address("chhapra","Bihar")
# a.location()
# a.getcity()
# # print(a.__city) #
# print(a.state)

#POLYMORPHISM
class Address:
  def __init__(self,city,state):
    self.city = city
    self.state = state
  def location(self):
    print(f"my address location is {self.city} in {self.state}")
 
class HomeTown:
  def __init__(self,city,state):
    self.city = city
    self.state = state
 
  def location(self):
    print(f"my home town location is {self.city} in {self.state}")
  
a = Address("vadodara","gujrat")
a.location()
b = HomeTown("chappra","bihar")
b.location()

# class Withdraw:
#   total = 0 # class variable
#   def __init__(self,city,state):
#     self.city = city
#     self.state = state
#     Withdraw.total += 1
 
#   def location(self):
#     print("location")
 
# a = Withdraw("jaipur","rajasthan")
 
# b = Withdraw("bhilwara","rajasthan")
 
# a.total

# overloading -> not possible

# def address(city,state):   # paramter -> 2
#     print(f"my address is {city} in {state}")

# def address(city,state,country):   # paramter -> 3
#     print(f"my address is {city} at {state} in {country}")

# # address("chappra","bihar")   # overloading possible nhi hai

# address("jaipur","rajasthan","india")


#overridding
# class Address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state

#     def location(self):
#         print("address locations")


# class User(Address):
#     def __init__(self,name,age,city,state):
#         super().__init__(city,state)
#         self.name = name
#         self.age = age

#     def location(self):    # over riding
#         print("user locations")


# u = User("arya mains",20,"kukas","rajasthan")
# u.location()

#immnutable -> not change
# t=(10,20,30)
# print(t[0])
# print(t[-1])

#example
#marks =[98,90,80,95]

#tuple
# t = tuple(marks)
# marks[3] = 50
# print(type(marks))
# print(marks)

# #tuple->not change
# t=tuple(marks)
# print(type(t))
# print(t)

# #tuple->list
# m=list(t)
# print(type(m))
#print(m)

