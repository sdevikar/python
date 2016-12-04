# A module is simply a python file (with .py extension)
# A module is imported by using import keyword
# Modules are loaded only once and initialized only once
# i.e. if the other module imports the same module, it will not be initialized again
#
# so local variables inside the module act as a "singleton" - they are initialized only once.

import urllib
import mymodule

connection = urllib.urlopen("http://www.learnpython.org/en/Modules_and_Packages")
#print "result = " + str(connection.info())
print "result code = "+str(connection.geturl())

# To make your own module, you just need to create a file with the module name

# To import the module, just use import command and filename without the extension
# To use the functions in the module, use <modulename>.<functionname>

print mymodule.add(3,4)
print mymodule.subtract(3,4)
print mymodule.divide(3,4)
print mymodule.multiply(3,4)
