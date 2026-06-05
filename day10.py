# import numpy as np
#list
# l =[1,2,3]
# print(l)

# #array 1d
# arr = np.array(l)
# print(arr)

#2d list
# l =[[1,2,3],[4,5,6]]
# print(l)

#2d array
# arr = np.array([l])
# print(arr)
# print(arr[0][0])

# import numpy as np

# 2D list(replacement of number)
# l = [[1,2,3],[4,5,6]]
# l[1][0] = 100

# print(l)
# print(l[1][0])

# 2D array (replacement of number)
# arr = np.array([[1,2,3],[4,5,6]])
# arr[1][0] = 100

# print(arr)
# print(arr[1][0])

#list
# l=[1,2,3]
# lm=l*2
# print(lm)

#array
# arr = np.array([l])
# arrM = arr*2
# print(arrM)

# comparsion
# import numpy as np
# import time
 
 
# # list
# start = time.time()
# l = [i*2 for i in range(1000000)]
# print("list output:",time.time() - start)
 
# # array
# start = time.time()
# arr = np.array(1000000)*2
# print("array output:",time.time() - start)

# #Zeros
# # zeros array 1d
# import numpy as np

# arr = np.zeros(5)
# print(arr)

# # zeros array 2d
# arr1 = np.zeros((3,4))
# print(arr1)

# #ones array 1d
# import numpy as np
# arr = np.ones(6)
# print(arr)
 
# #ones array 2d
# arr = np.ones((5,6))
# print(arr)

# #by help of zeros make 2d arry then add each by 10
# import numpy as np
# arr=np.zeros((3,4))+10
# print(arr)
 
# arr1=np.ones((3,4))*10
# print(arr1)
 
# #FULL FOR 1d
# import numpy as np
# arr = np.full((3),0)
# print(arr)
 
# #FULL FOR 1d
# import numpy as np
# arr = np.full((2,3),5)
# print(arr)
 
# #random for 1d 0 -> 1
# import numpy as np

# arr = np.random.random(5)
# print(arr)

# # random for 2d 0->1
# arr1 = np.random.random((2,3))
# print(arr1)

#arrange for 1d
# import numpy as np
# arr = np.arange(5)
# print(arr)

# #arange for 2d
# arr1 = np.arange(0,10,2)
# print(arr1)

# import numpy as np
# # vector 1d list
# l = [1,2,3]
# print(l)
# #vector 1d array
# arr = np.array(l)
# print(arr)
 
# #matrix 2d list
# l = [[1,2,3],[4,5,6]]
# print(l)
# #matrix 2d array
# arr = np.array(l)
# print(arr)
 
# #tensor 3d list
# l = [[[1,2],[3,4]],[[5,6],[7,8]]]
# print(l)
# #tensor 3d array
# arr = np.array(l)
# print(arr)

#array 
# import numpy as np
# arr = np.arange(12)#1d
# arr = np.arange(12).reshape(4,3)
# print ("shape:",arr.shape)
# print ("shape",np.shape(arr))
# print ("dimension",np.ndim(arr))
# print ("size",np.size(arr))
# print ("datatype:",arr.dtype)