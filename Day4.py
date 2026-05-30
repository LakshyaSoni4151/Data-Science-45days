# # def hello() :
# #     print("hello function is working")

# # hello() 


# #example
# # def hello1(a): # a as a parameter
# #     print(a)
# # hello1(100) # 100 as argument

# # def add(a,b):
# #     print(a+b)
# # add(10,5)

# # def add(a=2,b=3):
# #    print(a+b)
# # add(10,5)
# # add()

# #example

# # def power(a,b):
# #     print(a**b)

# # power(5,2)
# # power(2,5)
# # power(b=5,a=2)
# # power(a=2,b=5)


# #EXAMPLE
# # def student(*a):
# #     print(a)
# #     print(type(a))
# #     print(a[0])

# # student(1,2,3,4,5,6)
    
# #question

# # def marks(a):
# #     #for loop
# #     for i in a
# #     print (i)

# #     marks9([10,20,30,40,50])   

# # #question
# # def address(a):
# #     for i in a:
# #         for j in i:
# #             print(j)
# # address(["Hello","World"])  

# # #Example
# # def sum(a,b):
# #  return a+b

# # result 
# # sum(10,20)

# # Lambda Functions [lambda arguments : expression]

# # add = lambda x: x
# # print(add(100))


# # sum = lambda x, y: x + y
# # print(sum(10, 20))

# # a = lambda x:x
# # print(a([10,20,30,40]))

# #List comprehension
# #print([i for i in range(5)])
# #example

# # l = [10,20,30,40,50,60]
# # print([l[i]for i in range (len(l))])

# # #Question
# # l=[10,20,[30,40,50,60]]
# # print([l[2][i] for i in range (len(l[2]))])

# #LIST

# # l=[10,20,30,40]
# # print(l[0])
# # print(len(l))
# # #append
# # l.append(50)
# # print(l)
# # #insert
# # l.insert(2,23)
# # print(l)
# # print(l[-1])

# #question

# l = [10,20,30,{"name":"yourname","address":["jaipur","kukas","home town","friend house"]}]

# print(l)
# print(l[0])

# for i in l:
#     print(i)

# for i in l[3]["address"]:
#     print(i, end="",sep="")

# l=[10,20,30,[40,50,[60,70,80]]]
# print(l[3][0])
# print(l[3][1])

# for i in range(len(l[3])-1):
#     print(l[3][i])

#dictionary
# d = {"name":"hello","age":20}

# print(d.keys())
# print(d.values())

# for i in d.keys():
#     print("key=,i")
#     print("value=",d[i])

#question
# d = {
#     "Message": "Number of Post office(s) found: 5",
#     "Status": "Success",
#     "PostOffice": [
#         {
#             "Name": "Bali",
#             "Description": "",
#             "BranchType": "Sub Post Office",
#             "DeliveryStatus": "Delivery",
#             "Taluk": "Bali",
#             "Circle": "Bali",
#             "District": "Pali",
#             "Division": "Pali",
#             "Region": "Jodhpur",
#             "State": "Rajasthan",
#             "Country": "India",
#         },
#         {
#             "Name": "Boya",
#             "Description": "",
#             "BranchType": "Branch Post Office",
#             "DeliveryStatus": "Delivery",
#             "Taluk": "Bali",
#             "Circle": "Bali",
#             "District": "Pali",
#             "Division": "Pali",
#             "Region": "Jodhpur",
#             "State": "Rajasthan",
#             "Country": "India",
#         },
#         {
#             "Name": "Dantiwara",
#             "Description": "",
#             "BranchType": "Branch Post Office",
#             "DeliveryStatus": "Delivery",
#             "Taluk": "Bali",
#             "Circle": "Bali",
#             "District": "Pali",
#             "Division": "Pali",
#             "Region": "Jodhpur",
#             "State": "Rajasthan",
#             "Country": "India",
#         },
#         {
#             "Name": "Kot- Baliyan",
#             "Description": "",
#             "BranchType": "Branch Post Office",
#             "DeliveryStatus": "Delivery",
#             "Taluk": "Bali",
#             "Circle": "Bali",
#             "District": "Pali",
#             "Division": "Pali",
#             "Region": "Jodhpur",
#             "State": "Rajasthan",
#             "Country": "India",
#         },
#         {
#             "Name": "Sela",
#             "Description": "",
#             "BranchType": "Branch Post Office",
#             "DeliveryStatus": "Delivery",
#             "Taluk": "Bali",
#             "Circle": "Bali",
#             "District": "Pali",
#             "Division": "Pali",
#             "Region": "Jodhpur",
#             "State": "Rajasthan",
#             "Country": "India",
#         },
#     ],
# }

# print(d["Message"])
# print(d["Status"])

# for i in d["PostOffice"]:
#     print(i["Name"])
#     print(i["Taluk"])
#     print(i["Circle"])
#     print(i["District"])
#     print(i["Division"])
#     print(i["Region"])
#     print(i["State"])
#     print(i["Country"])
#     print("\n")
