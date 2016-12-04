# Sounds like dictionaries is another name for hash tables
# keys can be any type of object (i.e. string, number etc.)

# You define a dictionary using curly braces
phonebook = {}
phonebook["Tom"] = "(012)345-6789"
phonebook["Dick"] = "(123)456-7890"
phonebook["Harry"] = "(234)567-8901"

number = phonebook["Tom"]

print "Tom's number is: " + number

# Another way to define a dictionary is as follows (javascript style)
salaries = {
"student": 0,
"software enginner": 100000,
"lawyer": 500000
}
print "Lawyers earn: " + str(salaries["lawyer"])

# What can be used as key to the dictionary?
# Anything hashable
# That means immutable objects.
# e.g. string, integer, tuple are immutable
# lists are "mutable"


# How to iterate over a dictionary?
# note that the keys won't be iterated over sequentially
# in the following example, salary of software engineer is printed first

for key, value in salaries.iteritems():
    print "Salary for %s is %d" %(key, value)
