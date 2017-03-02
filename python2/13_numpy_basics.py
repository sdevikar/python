import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)

###
# This will create the following array:
# [
#  [ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
# ]
#
# Notice that we have 3 arrays of length 5 each.
# Read the array as follows:
# The last value in the shape tuple is the length of the innermost array
# The value to the left in the tuple i.e. 3 in (3,5) is the number of such arrays
###

b = np.arange(30).reshape(3, 5, 2)
print(b)

###
# This will create the following array
# [
#  [[ 0  1]
#  [ 2  3]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]]
#
# [[10 11]
#  [12 13]
#  [14 15]
#  [16 17]
#  [18 19]]
#
# [[20 21]
#  [22 23]
#  [24 25]
#  [26 27]
#  [28 29]]
# ]
# Notice that the reading method above still holds. i.e. in shape tuple (3,5,2)
# 2 is the length of the innermost array
# The value to its left, i.e. 5, is the number of the innermost array
# The value further to the left, i.e. 3, is the number of arrays of arrays of length 2


# Indexing the arrays
print(a[0]) # this should return the first row i.e. [0 1 2 3 4]
print(a[0:2]) # this should return row 0 and row 1. Row 2 is not included

# in order to specify an individual element, row and column indexes,
# which are called axes in numpy arrays, should be specified as comma separated values
print("a[0,1] = {}".format(a[0,1])) # this should return 1
print("a[0,1] = {}".format(a[0][1])) # this is the same as a[0,1]

# So, in order to access 15 in array b, we can do the following
print("b[1,2,1] = {}".format(b[1,2,1]))
