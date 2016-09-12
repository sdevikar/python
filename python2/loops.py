# We will test the loops in this file.
# Python also has for and while loop.

# For loop:

names = ["Ramesh", "Suresh", "Ganesh", "Jignesh"]

for name in names:
    print name

# prints 0 to 4 using range function which returns a  "list"
# passing a single argument works
list = range(5)
for x in list:
    print x

print "---"
# print 5 to 10 using range function, which takes two arguments and returns a
# list
list = range(5, 11)
for x in list:
    print x
print "---"
# prints 0 to 5, using xrange function, which accepts a single argument
# and returns an "iterator" over a list of
iterator = xrange(6)
for x in iterator:
    print x
print "---"

# print 5 to 10 using xrange with two arguments
iterator = xrange(10,15)
for x in iterator:
    print x
print "---"

# what happens when float argument is passed to range?
# an error will be returned at below line
#list = range(5.5)

# While loops are the same as in any other language:
print "Begin while loops demo..."
count = 0
while count < 5:
    #count++ # count ++ doesn't work in python
    count += 1
    print count
print "---"

# break statement
print "Let's test the break statement..."
for name in names:
    print name
    if name == "Suresh":
        print "Name found"
        break
print "---"

# We'll skip continue, because we rarely use it

# Else can be used in the loops..
# The loop iterates over all the values in the iterable and then else clause
# is executed.
# We can take advantage of this behavior in search functionality.
# If the item we are searching for is not present in the iterable datastrcuture,
# we can raise an error or something in the else part.
for name in names:
    # try to find a name that doesn't end with "sh"
    if not(name.endswith("sh")):
        # this will never be executed because all our names end with "sh"
        break
else:
    print "Found no names that don't end with sh... well, damn!"

print "---"

# Another simpler example:
# Here, if condition is satisfied. So break will be executed
# loop was never completely iterated over and therefore, else clause of the loop
# will never be executed

for x in range(10):
    if x == 5:
        print "breaking the loop at: " + str(x)
        break;
    else:
        print "counting loop: " + str(x)
else:
    # This will never be executed beause the loop was terminated before it
    # could completely iterate over the list.
    print "This will not be executed"

print "---"
# Else clause is available for while loop as well
count = 0
while count < 5 :
    count += 1
else:
    print "Count exceeded "
