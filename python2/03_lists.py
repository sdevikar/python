# Create a simple list
# Also prove that the variables in the list have no fixed type

mylist = ['a', 'b', 'c']
mylist.append(2)
mylist.append(4)
mylist.append(6)
mylist.append("swapnil")
mylist.append(3.4)

print mylist[0]
print mylist[6]

print "*****"

for item in mylist:
    print item

myname = mylist[6]

print "my name is " + myname

numberfloat = 1 + 2 * 3 / 4.0
numberint = 1 + 2 * 3 / 4

print "answer to int calculation is " + str(numberint) + " and float calculation is " + str(numberfloat)
