# import matplotlib.pyplot as plt
# x=[2010,2015,2020,2025]  #x cord
# y=[100,200,250,300]   #y cord
# plt.plot(x,y)  #Line graph
# plt.xlabel("years")   #x label
# plt.ylabel("sales")  #y label
# plt.title("sales report")  #graph title

# plt.show()  #Graph show


# import matplotlib.pyplot as plt
# x=[2010,2015,2020,2025]  #x cord
# y=[100,200,250,300]   #y cord

# #graph size
# plt.figure(figsize=(6,4))   #width,height
# plt.plot(x,y)  #Line graph
# plt.show()

# import matplotlib.pyplot as plt
# x = [2010,2015,2020,2025] # x cord
# y = [100,200,250,300] # y cord.
 
# #
# # **Markers**
 
# # |character      |  |  |description |
# # |-------------|  -------------------------------|
# # |'.'       | | |point marker|
# # |','       | | |pixel marker|
# # |'o'       | | |circle marker|
# # |'v'       | | |triangle_down marker|
# # |'^'       | | |triangle_up marker|
# # |'<'       | | |triangle_left marker|
# # |'>'       | | |triangle_right marker|
# # |'1'       | | |tri_down marker|
# # |'2'       | | |tri_up marker|
# # |'3'       | | |tri_left marker|
# # |'4'       | | |tri_right marker|
# # |'8'       | | |octagon marker|
# # |'s'       | | |square marker|
# # |'p'       | | |pentagon marker|
# # |'P'       | | |plus (filled) marker|
# # |'*'       | | |star marker|
# # |'h'       | | |hexagon1 marker|
# # |'H'       | | |hexagon2 marker|
# # |'+'       | | |plus marker|
# # |'x'       | | |x marker|
# # |'X'       | | |x (filled) marker|
# # |'D'       | | |diamond marker|
# # |'d'       | | |thin_diamond marker|
# # |'|'       | | |vline marker|
# # |'_'       | | |hline marker|
 
# # **Line Styles**
 
# # |character      |  |  |  |description |
# # |-------------|   -------------------------------|
# # |'-'       | | | |solid line style|
# # |'--'      | | | |dashed line style|
# # |'-.'      | | | |dash-dot line style|
# # |':'       | | | |dotted line style|
 
# # Example format strings:
 
# #     'b'    # blue markers with default shape
# #     'or'   # red circles
# #     '-g'   # green solid line
# #     '--'   # dashed line with default color
# #     '^k:'  # black triangle_up markers connected by a dotted line
# # **Colors**
 
# # |character      |  |  |  |color |
# # |-------------|   -------------------------------|
# # |'b'       | | | |blue|
# # |'g'       | | | |green|
# # |'r'       | | | |red|
# # |'c'       | | | |cyan|
# # |'m'       | | | |magenta|
# # |'y'       | | | |yellow|
# # |'k'       | | | |black|
# # |'w'       | | | |white|
# # graph size
# plt.figure(figsize=(6,2)) # width or height
# plt.plot(x,y,color="y",marker='*',linestyle=":",linewidth=4,markersize=14,)
# plt.show()


# #multi lines chart
# import matplotlib.pyplot as plt

# x=[2010,2015,2020,2025]
# y1=[100,200,260,290]
# y2=[150,185,195,300]

# plt.plot(x,y1,label="jeans")
# plt.plot(x,y2,label="shirt")
# plt.legend()  #info of label
# plt.show()


# #BAR CHART
# import matplotlib.pyplot as plt
# x=[2010,2015,2020,2025]
# y=[100,150,200,290]

# #size
# plt.figure(figsize=(6,2))
# plt.bar(x,y)
# plt.show()


# # multi bar chart
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([1,2,3,4])
# y1 = [10,20,20,40]
# y2 = [20,30,25,30]
# # calculation -> width
# w = 0.40
# plt.bar(x - w/2,y1 , label="boys",width=w) # hide second
# plt.bar(x + w/2,y2, label="girls",width=w) # show
 
# plt.xlabel("groups")
# plt.ylabel("number of students")
# plt.title("Number of Students in Each group")
# plt.legend()
# plt.show()
 