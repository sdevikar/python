# simple arithmetic operations:
number = 1+2*3/4.0
print number

# using operators with strings
print "My name is " + "Swapnil " + "Devikar"

# *interesting* print the same string multiple times
print "Don't Stop! " * 5


# *interesting* support for repeating the list
# this will create a list that repeats the original list 3 times
print [1, 2, 3] * 3

# Exercise
# create two lists called x_list and y_list, which contain 10 instances of the
# variables x and y, respectively. You are also required to create a list called
# big_list, which contains the variables x and y, 10 times each, by
# concatenating the two lists you have created.

x = 3
y = 2

x_list = [x] * 10
print x_list

y_list = [y] * 10
print y_list

big_list = x_list + y_list
print big_list
