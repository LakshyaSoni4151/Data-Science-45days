# csv file import from github
# import pandas as pd

# url = "https://raw.githubusercontent.com/LakshyaSoni4151/Data-Science-45days/main/file2.json"

# df = pd.read_json(url)

# print(df)

# #head -> starting 5 rows
# #print (df.head())
# #head -> 2 rows data
# print(df.head(-2))
# #head->negative number


#Tail
# import pandas as pd

# url = "https://raw.githubusercontent.com/LakshyaSoni4151/Data-Science-45days/main/file2.json"

# df = pd.read_json(url)
# df
# #tail is used to get last 5 rows data
# print (df.tail(2))

#SHAPE
# import pandas as pd

# url = "https://raw.githubusercontent.com/LakshyaSoni4151/Data-Science-45days/main/file2.json"

# df = pd.read_json(url)
# print (df.shape)

# #INFO
# import pandas as pd
# import numpy as np
# url = "https://raw.githubusercontent.com/LakshyaSoni4151/Data-Science-45days/main/file2.json"

# df = pd.read_json(url)
# df["Salary"]=[100,200,300,np.nan,500]
# print (df.info())
# # print (df.info(verbose=False))

#RENAME
# import pandas as pd

# url = "https://raw.githubusercontent.com/LakshyaSoni4151/Data-Science-45days/main/file2.json"

# df = pd.read_json(url)
# print (df.rename(columns={"name":"student_name","marks":"salary"},inplace=True))
# #original variable df -> value same
# print (df)

#DESCRIBE
# import pandas as pd

# url = "https://raw.githubusercontent.com/LakshyaSoni4151/Data-Science-45days/main/file2.json"

# df = pd.read_json(url)
# print (df.describe(include=[]))

#practice questiom
# import pandas as pd

# data = {
#     "Emp ID": [101, 102, 103, 104, 105, 106],
#     "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
#     "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
#     "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
#     "Experience": [2, 3, 5, 4, 1, 3]
# }

# df = pd.DataFrame(data)

# # Head (first 5 rows)
# print("Head:")
# print(df.head(2))

# # Tail (last 5 rows)
# print("\nTail:")
# print(df.tail(2))

# # Shape (rows, columns)
# print("\nShape:")
# print(df.shape)

# # Rename column
# df.rename(columns={"Emp ID": "Employee_ID"}, inplace=True)
# print("\nAfter Rename:")
# print(df)

# # Info
# print("\nInfo:")
# df.info()

# # Describe
# print("\nDescribe:")
# print(df.describe())

# import pandas as pd

# url = "https://raw.githubusercontent.com/LakshyaSoni4151/Data-Science-45days/main/file2.json"
# df = pd.read_json(url)
# #get single column data
# df["name"]
# #add single column
# df["salary"] = df["marks"] +100
# #add sinble column
# df["salary"] = [100,200,300,400,500]
# print (df)

#add colunm
# import pandas as pd
# d = {
#     "name":["vishal","virat","vineet"], # 3 rows
#     "salary":[100,200,300] # 3 rows
# }
# df = pd.DataFrame(data=d)
# # df["marks"] = [10,20,30]
# df["marks"] = df["salary"] / 2
# print (df)