# import pandas as pd

# d = {
#     "name":["vishal","virat","vineet"], # 3 rows
#     "salary":[100,200,300] # 3 rows
# }

# df = pd.DataFrame(data=d)

# df["holidays"] = df["salary"] / 100
# df["decrement"] = [10,20,30]
# #delete col
# df.drop(["salary", "name"], axis=1, inplace=True)
# print(df)

# import pandas as pd

# d = {
#     "name":["vishal","virat","vineet"], # 3 rows
#     "salary":[100,200,300] # 3 rows
# }

# df = pd.DataFrame(data=d)
#print(df)
#print(df.loc[2,"name"])
#print(df.iloc[2,0])
#get single row data
#print(df.iloc[1])
##get single roe using loc
# print(df.loc[1])

# #get multi rows using iloc
# print(df.iloc[0:3])

# #get multi rows using loc
# print(df.loc[0:3])

##sub data get using iloc
# df1 = df.iloc[0:2,[0]] #rows -> 0,1 and cols->0 | name
# print(df1)

# df2 = df.loc[0:1, ["name"]]
# print(df2)

#import pandas as pd
 
# d = {
#     "name": ["Amit", "Riya", "Raj", "Sara", "Vineet"],
#     "salary": [50000, 45000, 60000, 55000, 48000],
#     "Experience": [2, 3, 5, 4, 1]
# }
# df = pd.DataFrame(data=d)
# print("Original DataFrame:")
# print(df)
# print(df.iloc[0:3]) #first 3 rows
 
# print(df.iloc[1]) #  secound row
 
# print(df.loc[0:2]) # row using 0 to 2
 
# print(df.iloc[0:2]) # using 0 to 1
 
# print(df["salary"]) # salary
 
# print(df[["name", "salary"]])
 
# df.loc[0, "salary"] = 55000 # here we are updating the salary
 
# df.loc[2, "Experience"] = 6
 
# print(d) # after data is updated

import pandas as pd
url = "https://raw.githubusercontent.com/LakshyaSoni4151/Data-Science-45days/main/student-data.json"
df = pd.read_json(url)
# print(df)
# print()
# #data of all  Male
# print("data of all  Male")
# print()
# male_names = df.loc[df["gender"] == "Male", "name"]
# print(male_names)

#filter 1
print (df[df["english"]==95])

#filter 2
print (df[df["maths"]<60])

#filter 3
print(df[df["physics"]<= 56])

print (df[(df["maths"] >90) & (df["english"] >90)])
 
