# packages are simply directories that can  contain modules and other packages
# the only secret is that you have to create __init__.py module inside the package directory

# the following works, but requies you to specify package name when calling a function
import mypackage.p_mymodule

# like this...
mypackage.p_mymodule.greeting()


# the following works too and does not require you to use the package name
from mypackage import p_mymodule

p_mymodule.greeting()
