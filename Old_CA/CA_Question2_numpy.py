import numpy as np

# a
array = np.arange(1,801).reshape(200,4)
print(array)

# b
array_split = np.vsplit(array,5)
print(array_split)

#c
array_split[0] = array_split[0].reshape(8,20)
print(array_split[0])

array_split[1] = array_split[1].reshape(20,8)
print(array_split[1])

array_split[2] = array_split[2].reshape(16,10)
print(array_split[2])

print(array_split)


# d
print("\n\nd ::")
array_hsplit1 = np.hsplit(array_split[0],2)
print(array_hsplit1)
array_hsplit2 = np.hsplit(array_split[0],4)
print(array_hsplit2)