#Python uses C style string formatters. i.e. %s is used for strings
myname = "Swapnil"

#this will print Hello, my name is %s
print "Hello, my name is %s"

#this will print: Hello, my name is Swapnil
print "Hello, my name is %s" %myname

#Can we cheat?
# Yes, all of this works
x = 5
y = 10
z = 3.3
print "Hello, my name is %s" % x
print "Hello, my number is %d" % x
print "Hello, my number is %x" % y
print "Hello, my number is string: %s" % z
print "Hello, my number is integer: %d" % z
print "Hello, my number is float: %f" % z
print "Hello, my number is float: %.3f" % z

# but how about strig to number?
# the below will result in an error
# print "Hello, my name is %d" % myname

# SO, I guess python will perform conversions for us, wherever it can

# Using two or more arguments
print "Hello, my name is %s and number is %d" % (myname, x)
print "Hello, my name is %s and number is %s" % (myname, x)

# A list can be formatted as a string as well
list = [1, 2, 3]
print list

# Exercise
# You will need to write a format string which prints out the data using the
# following syntax: Hello John Doe. Your current balance is 53.44$.
name = "John Doe"
balance = 53.44
currency = "$"

print "Hello %s. Your current balance is %.2f%s" % ( name, balance, currency)
