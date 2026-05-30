# d={"age":20,"name":"hello"}
# d.update({"name":"arya mains"})
# d['name']= "arya mains new"
# del d['name']
# print(d)

#nested dict
# d={"address":{"address1":{"city":"kukas city","district":"jaipur"},
#               "address2":{"city":"gopalpura","district":"arya mains"}
#               }
#               }

# print (d["address"]["address1"]["city"])
# print (d["address"]["address1"]["district"])
# print (d["address"]["address2"]["city"])
# print (d["address"]["address2"]["district"])

#NESTED LIST

# l=[10,20,30,["hello","hello1","hello2",[True,False]]]
# print(l)
# #SLICING

# l1=l[:3]
# print(l1)
# #example
# print(l[2:])
# print(l[3][1:3])

#function
# def square(x):
#     return x * x
# #map (2 arguments)
# l = [10,20,30]

# l1 = list(map(square,l))

# print(l1)

# #example 
# #map (2 arguments)
# l = [10,20,30]
# l1= list(map(lambda x:x*x,l))
# print(l1)

# l1 =[]
# for i in range(len(l)):
#     l1.append(l[i] * l[i])
#     print(l1)

# #     #filter
# def helo(x):
#      return x.endswith('a')

# l = ["apple","banana","cat","dog"]

# l1 = list(filter(helo,l))

# print(l1)

# #example
# l1 =[]
# for i in l:
#     if 'a' ==i[-1]:
#         l1.append(i)
# print(l1)

#FILE HANDLING AND EXCEPTION HANDLING

#try except
# try:
#     num1 = 10
#     num2 = 5
#     print(num1/num2)
# except:
#     print("hello except")

#     #try except
# try:
#     num1 = 10
#     num2 = 0
#     print(num1/num2)
# except:
#     print("hello except")

#     #try except final
# try:
#     num1 = 10
#     num2 = 5
#     print(num1/num2)
# except:
#     print("hello except")
# finally:
#     print("hello finally divide")