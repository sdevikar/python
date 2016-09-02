# booleans
x = 3
print x == 2

# proper indentation in python is essential
if x == 2:
    print "x is indeed 2"
    print "it's insane that the if block is determined by indentation"
        # print "this will give me an error"
print "So, this will be printed regardless of x == 2"

# combining boolean expressions
y = 5

if x == 2 and y == 5:
    print "Think positive"
elif x == 3 and y == 5:
        print "Life's okay, I guess"
else:
    print "That's it, I'm done!"

# iterating using in operator
name = "SlimShady"
rappers = ["SlimShady", "TheRealSlimShady", "Eminem"]

if name in rappers:
    print "He's from Detroit"
else:
    print "He's not a real rapper"

# comparing values vs objects
x = [1, 2, 3]
y = [1, 2, 3]

if x == y:
    print "x and y are equal in terms of their values"

if x is y:
    print "x and y are the same object"
else:
    print "they're different objects though"

# the not operator
if True is not False:
    print "This concludes the chapter"
    print not False
    print not True
