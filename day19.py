# import matplotlib.pyplot as plt
# import numpy as np
 
# x= np.array([1, 2, 3, 4]) # x cord
# y1 = [10, 20, 20, 40]
# y2 = [20, 30, 25, 30] # y cord
# y3 = [30, 40, 35, 20]
 
# w = 0.90
# plt.bar(x-w/3, y1, width=w/3, label="Boys")# bottom = y1
# plt.bar(x, y2, width=w/3, label="Girls")
# plt.bar(x+w/3, y3, width=w/3, label="Others")
 
# plt.xlabel("Groups")
# plt.ylabel("No of students")
# plt.title("Students in each group")
# plt.legend()
# plt.show()

# # pie chart percentage
# import matplotlib.pyplot as plt

# fruits = ['apple','banana','orange','watermelon']
# count = [40,30,15,70]

# colors = ["red","yellow","orange","green"]

# plt.pie(count, labels=fruits, colors=colors, startangle=90, autopct="%1.1f%%")
# plt.show()

import matplotlib.pyplot as plt

#SUBPLOT
# FIRST CHART

# x = [1,2,3,4,5]
# y = [10,20,30,40,55]
 
# plt.subplot(1,2,1) # row,cols,position
# plt.plot(x,y)
# plt.xlabel("x axis")
# plt.ylabel("y axis")
 
# # second chart
# x1 = ['apple','banana','orange','watermelon']
# y1 = [40,30,15,70]
 
# plt.subplot(1,2,2) # row,cols, position
# plt.pie(y1,labels=x1,startangle=90)
# plt.xlabel("x1 axis")
# plt.ylabel("y1 axis")
# plt.tight_layout()
# plt.show()


# import matplotlib.pyplot as plt
 
# # subplot
# # first chart
# x = [1,2,3,4,5]
# y = [10,20,30,40,55]
 
# plt.subplot(2,2,1) # row,cols,position
# plt.plot(x,y)
# plt.xlabel("x axis")
# plt.ylabel("y axis")
 
# # second chart
# x1 = ['apple','banana','orange','watermelon']
# y1 = [40,30,15,70]
 
# plt.subplot(2,2,2) # row,cols, position
# plt.pie(y1,labels=x1,startangle=90)
# plt.xlabel("x1 axis")
# plt.ylabel("y1 axis")
 
# # third chart
# x = [1,2,3,4,5]
# y = [10,20,30,40,55]
 
# plt.subplot(2,2,3) # row,cols,position
# plt.plot(x,y)
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# # fourth chart
# x1 = ['apple','banana','orange','watermelon']
# y1 = [40,30,15,70]
 
# plt.subplot(2,2,4) # row,cols, position
# plt.pie(y1,labels=x1,startangle=90)
# plt.xlabel("x1 axis")
# plt.ylabel("y1 axis")
 
 
# plt.tight_layout()
# plt.show()

