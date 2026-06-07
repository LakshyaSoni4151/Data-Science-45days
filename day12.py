#sort
#1d
# import numpy as np
# arr = np.array([10,40,30,60,90,7,5])
# print(arr)
# arr_s = np.sort(arr)
# print(arr_s)

#2d by default sort will done in row wise in ascending
#axis = 0 -> cols
#axis = 1 -> rows

# import numpy as np
# arr1 = np.array([[5,6,20],[40,9,4]])
# print(arr1)
# arr1_s = np.sort(arr1 , axis =1)
# print(arr1_s)

#example
# sort 2d
# import numpy as np
# arr=np.array([[5,60,-2],[3,4,1]])
# print(arr)
# sort_arr=np.sort(arr)
# print(sort_arr)
# # by default sorting is ascending
 
 
# # descending sort
# import numpy as np
# arr= np.array([45,12,78,23,46])
# print(arr)
# descen_arr=np.sort(arr)[::-1]
# print(descen_arr)

#filter
# import numpy as np 
# arr = np.array([10,20,40,6,3,4,2])
# print(arr)
# arr_f = arr[arr<20]
# print(arr_f)

# # example
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8])
# even=arr[arr%2==0]
# print(even)

#FANCY INDEXING VS NP.WHERE()
# import numpy as np 
# arr = np.array([10,20,3,4,90,100])
# print(arr)
# arr_f = arr[[0,2]] # 0 index value, 2 index value]
# print(arr_f)

# #np.where
# import numpy as np

# # 1d
# arr = np.array([10,3,4,80,30,40,9])
# print(arr)

# arr_w = np.where(arr>40,"True","False")  # condition : True : false
# print(arr_w)

# # example

# arr1 = np.array([10,3,4,80,30,40,9])
# print(arr1)

# arr_w = np.where(arr>40,arr+2,arr-2)  # condition : True : false

# # if (arr>40):
# #     arr+2
# # else:
# #     arr-2

# print(arr_w)

#concatenate
# #1d
# import numpy as np
# arr1 = np.array([10,20,30])
# arr2 = np.array([1,2,3])
# arr1_arr2 = np.concatenate ((arr1,arr2 ))
# print(arr1_arr2)

# #manually
# arr1_arr2_new = arr1 + arr2
# print(arr1_arr2_new)

# #2D
# arr = np.array([[1,2,3],[4,5,6]])
# arr1 = np.array([[7,8,9],[4,8,5]])
# arr_arr1 = np.concatenate((arr,arr1), axis=0)
# print(arr_arr1)

#Statistical Functions**
# import numpy as np

# a = np.array([10, 20, 30, 40, 50])

# # 1. np.sum(a)
# print("Sum =", np.sum(a))
# # Output: 150

# # 2. np.mean(a)
# print("Mean =", np.mean(a))
# # Output: 30.0

# # 3. np.median(a)
# print("Median =", np.median(a))
# # Output: 30.0

# # 4. np.min(a)
# print("Min =", np.min(a))
# # Output: 10

# # 5. np.max(a)
# print("Max =", np.max(a))
# # Output: 50

# # 6. np.var(a)
# print("Variance =", np.var(a))
# # Output: 200.0

# # 7. np.std(a)
# print("Standard Deviation =", np.std(a))
# # Output: 14.142135623730951

# # 8. np.prod(a)
# print("Product =", np.prod(a))
# # Output: 12000000

# # 9. np.cumsum(a)
# print("Cumulative Sum =", np.cumsum(a))
# # Output: [ 10  30  60 100 150]

# # 10. np.cumprod(a)
# print("Cumulative Product =", np.cumprod(a))
# # Output: [      10      200     6000   240000 12000000]

# # 11. np.argmin(a)
# print("Index of Min =", np.argmin(a))
# # Output: 0

# # 12. np.argmax(a)
# print("Index of Max =", np.argmax(a))
# # Output: 4

# # 13. np.abs(a)
# b = np.array([-10, -20, 30, -40, 50])
# print("Absolute Values =", np.abs(b))
# # Output: [10 20 30 40 50]

# # 14. np.unique(a)
# c = np.array([10, 20, 20, 30, 30, 40])
# print("Unique Values =", np.unique(c))
# # Output: [10 20 30 40]

# # 15. np.percentile(a, 50)
# print("50th Percentile =", np.percentile(a, 50))
# # Output: 30.0

# # 16. np.quantile(a, 0.5)
# print("0.5 Quantile =", np.quantile(a, 0.5))
# # Output: 30.0

# # 17. np.ptp(a)
# print("Range =", np.ptp(a))
# # Output: 40

# # 18. np.any(a)
# d = np.array([False, False, True, False])
# print("Any True =", np.any(d))
# # Output: True