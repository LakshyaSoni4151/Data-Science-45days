# #reshape array
# import numpy as np
# arr = np.arange(12) #-> 12 CAN BE 3*4,4*3
# up_arr = np.reshape(arr,(3,4))
# print(up_arr)

# #example 2d
# arr1=np.arange(24)

# up_arr1=np.reshape(arr1,(4,6))

# print(up_arr1)
# #Example 3d
# arr2=np.arange(24)

# up_arr2=np.reshape(arr1,(2,3,4))

# print(up_arr2)

#flatten : create copy then work
# import numpy as np
# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr = arr.flatten()
# print(up_arr)
# print(arr)

#3d
# import numpy as np
# arr = np.arange(24).reshape(2,3,4,)
# print(arr)
# up_arr = arr.flatten()
# print(up_arr)
# print(arr)

#ravel : work on original array
# import numpy as np

#example 2d
# arr = np.arange(14).reshape(7,2)
# print (arr)
# up_arr = arr.ravel()

# print( up_arr)

# #example 3d

# arr1 = np.arange(24).reshape(2,3,4,)
# print (arr1)
# up_arr1 = arr1.ravel()

# print( up_arr1)

#transpose
# import numpy as np
# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr = arr.T
# print (up_arr)

#3d
# import numpy as np
# arr = np.arange(24).reshape(2,3,4)
# print(arr)
# up_arr = arr.T
# print (up_arr)

#SLICING
#slicing for 1d
# import numpy as np
# arr = np.arange(11)
# print (arr)
# up_arr = arr[:3]
# print(up_arr)

#slicing for 2d
# import numpy as np
# arr1 = np.arange(16).reshape(8,2)
# print (arr1)
# up_arr1 = arr[:3]
# print(up_arr1)

#slicing for 3d
# import numpy as np
# arr2 = np.arange(36).reshape(4,3,3)
# print (arr2)
# up_arr2 = arr2[:3]
# print(up_arr2)

# print(arr2[0,0,0])  # 0
# print(arr2[2,1,2])  # 23

#while loop
#while loop for 1d
# import numpy as np
# arr = np.arange(12)
# i=0
# while i<len(arr):
#     print(arr[i], end =" ")
#     i +=1

# # while loop for 2d
# # while loop for 2d
# import numpy as np

# arr1 = np.arange(12).reshape(3,4)
# i = 0

# while i < 3:
#     j = 0

#     while j < 4:
#         print(arr1[i][j], end=" ")
#         j += 1

#     i += 1
    #while loop for 3d
# while loop for 3d
# import numpy as np

# arr2 = np.arange(36).reshape(4,3,3)

# i = 0
# while i < len(arr2):
#     j = 0
#     while j < len(arr2[i]):
#         k = 0
#         while k < len(arr2[i][j]):
#             print(arr2[i][j][k], end=" ")
#             k += 1
#         print()
#         j += 1
#     print()
#     i += 1

# #for loop
# #print 1d array
# import numpy as np
# arr = np.arange(12)
# for i in arr:
#   print(i, end=" ")
# print()
# print()
 
# #print 2d
# import numpy as np
# arr = np.arange(12).reshape(3,4)
# for i in arr:
#   for j in i:
#     print(j, end=" ")
#   print()
# print()
 
 
# #print 3d array
# import numpy as np
# arr = np.arange(24).reshape(2,3,4)
# for i in arr:
#   for j in i:
#     for k in j:
#       print(k, end=" ")
#     print()
#   print()
 
