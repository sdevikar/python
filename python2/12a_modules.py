# A module is simply a python file (with .py extension)
# A module is imported by using import keyword
# Modules are loaded only once and initialized only once
# i.e. if the other module imports the same module, it will not be initialized again
#
# so local variables inside the module act as a "singleton" - they are initialized only once.

import urllib
import mymodule
import mymodule2

connection = urllib.urlopen("http://www.learnpython.org/en/Modules_and_Packages")
#print "result = " + str(connection.info())
print "result code = "+str(connection.geturl())

# To make your own module, you just need to create a file with the module name

# To import the module, just use import command and filename without the extension
# To use the functions in the module, use <modulename>.<functionname>
print "Magic number in the module: %d" % mymodule.magic_number

print mymodule.add(3,4)
print mymodule.subtract(3,4)
print mymodule.divide(3,4)
print mymodule.multiply(3,4)

# You can import one module inside the other
from mymodule2 import average

# mymodule2 loads mymodule. But we'd expect that mymodule is loaded only once.
# this should NOT print 2
print "Magic number in the module: %d" % mymodule.magic_number

list = [1,2,5,7,8,10,15, -3]
x = mymodule2.average(list)

print x


# Exercise
# In this exercise, you will need to print an alphabetically sorted list of all functions in the re module,
# which contain the word find.
import re

#import dir
function_list = dir(re)
for function in function_list :
    print function
