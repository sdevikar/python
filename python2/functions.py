# Blocks in python:
# As seen earlier, python uses blocks (indentation) for loops and if else
# functions are the same. In general, python blocks are formatted as follows:
# <block keywoard> <block name>(arg1, arg2, ...) :
# Where
# <block keyword>:  keyword like "if", "while", "for", "def"
# <block name> :    For functions, it'll be function name."if", "while" etc.
#                   don't need it
# ()            :   Mandatory round braces

def default_greeting():
    print "Hello from myfunction!"

def user_greeting(username, greeting):
    # print message #  Even though "message" doesn't exist, no error will be
                    #  thrown, until this function is called
    print username + " says " + "\"" + greeting + "\""

def add(arg1, arg2):
    return arg1 + arg2



# How to call a function?

# is the round braces necessary?
# Yes, without round braces, nothing will happen.
# This is like declaring a variable
default_greeting

# print default greeting
default_greeting()

# print user greeting
user_greeting("Swapnil", "Welcome fall!")

# Make use for return value
answer = add(2, 3)
print "The answer is: " + str(answer)


#Exercise
#In this exercise you'll use an existing function, and while adding your own to
# create a fully functional program.

# Add a function named list_benefits() that returns the following list of
# strings: "More organized code", "More readable code", "Easier code reuse",
# "Allowing programmers to share and connect code together"
# Add a function named build_sentence(info) which receives a single argument
# containing a string and returns a sentence starting with the given string and
# ending with the string " is a benefit of functions!"

# Run and see all the functions work together!

def list_benefits():
    return [    "More organized code",
                "More readable code",
                "Easier code reuse",
                "Allowing programmers to share and connect code together"
            ];

def build_sentence(info):
    print info + " is a benefit of functions"

benefits = list_benefits()

for this_benefit in benefits:
    build_sentence(this_benefit)    
