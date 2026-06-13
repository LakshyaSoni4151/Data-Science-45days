# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
# df = pd.read_json(url)
# # by default ascending
# df.sort_values("english")
 
# # decending
# df.sort_values("english",ascending=False)
 
# # by default ascending method 1
# df.sort_values(by=['english'],ascending=[False])
 
# # multiple cols sort
# df.sort_values(by=['english','maths'],ascending=[False])
 
# # a to z
# df['name'] = df['name'].str.lower()
# df.sort_values("name")

# #add column total = py+maths+english
# df['total']= df['english']+df['maths']+df['english']
# print(df)

# # add row
# df.loc[14] = ['rajendra','Male',50,80,80,210]

# # update column
# df["name"] = df["name"].str.upper()

# # update row
# df.loc[14] = ['Rajendra','Male',60,90,85,235]

# # delete column
# df.drop("total",axis=1)

# # delete row
# df.drop(14,axis=0)

# #delte row and column simulataneously
# df.drop(14, axis=0).drop("total", axis=1)


# df.loc[df.index[:6], 'doj'] = [
#     '2025-01-01','2025-02-02','2025-03-03',
#     '2025-04-04','2025-05-05','2025-06-06'
# ]
# print(df)


import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df['doj'] = ['2025-01-10','2025-02-10','2025-03-10','2025-04-10','2025-05-10']
# df['doj'].dtype

# #convert string to date
# df['doj']=pd.to_datetime(df['doj'])
# df['doj'].dtype

# #date operation
# df['doj'].dt.year
# df['doj'].dt.month
# df['doj'].dt.day
# df['doj'].dt.day_name()

#20days
# df['doj']=pd.to_timedelta("20 days")
pd.to_timedelta(20,unit='D')
 
print(df)