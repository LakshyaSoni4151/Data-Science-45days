# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
 
# #anjali ->marks=null

# # import numpy as np

# # df.loc[4,"marks"] = None
# # df.loc[3,"roll no"] = None

# # # df.isnull()
# # # print(df)

# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# df.isnull()
# # sum
# df.isnull().sum()

# # drop null values by row
# df.dropna()

# # drop null values by cols
# df.dropna(axis=1)

# # fill by zero
# df.fillna(0)

# # fill by 100
# df.fillna(100)
# df

# # roll no -> 200 | marks -> 100 -> fillna
# # method 1
# # df["roll no"] = df['roll no'].fillna(200)
# # df['marks'] = df['marks'].fillna(100)
# # df

# #method 2
# # df.fillna({"roll no":200,"marks":100},inplace=True)
# # df

# # marks -> mean | nan fill with average
# mm = df['marks'].mean()
# df["marks"] = df['marks'].fillna(mm)
# df

# # aggregation
# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# # manually
# df['marks'].sum()
# df['marks'].mean()
# df['marks'].min()
# df['marks'].max()
# # usin aggregation
# df['marks'].agg(["sum","mean","min","max"])

# # concatenate
# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# df1 = pd.read_json(url)
# # pd.concat([df,df1]) # row
# pd.concat([df,df1],axis=1)

# # name -> cols 2 -> abhishek -> rajendra


# import matplotlib.pyplot as plt
# score = [10,20,30,40]
# over = [1,2,3,4]
# plt.plot(score,over)

# plt.show()
