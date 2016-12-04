message = "0123456789abcdef10-11-12"

# length of the string
length = len(message)
print "Length of string: %d" %(length)

# Finding index of characters within the string
index = message.index("a")
print "Index of letter a: %d" % index

index = message.index('b')
print "Index of letter b: %d" % index

# counting number of occurances of a letter in a string
repcount = message.count('-')
print "Number of times \"-\" occurred: %d" % repcount

print "**substrings**"
# printing a substring [start:end] start index is included, end is excluded
print message[5]
print message[7]
print message[5:7]
print message[5:7:1]
print message[5:1000]

# printing a substring in 'steps'
print ""
print "**substrings with steps**"
start = 3
end = 12
step = 2
print message[3]
print message[12]
print message[3:12:2]
print message[start:end:step]

print "**negative indices**"
# negative index in the string means index with respect to the end
print message[-1]  # start at -1

# reversing the string
print message[12:0:-1]  # going from 12 to 0 in reverse direction
print message[::-1]  # I guess the default start position is length of string and default end is -1

#let's put this theory to test
print message[6::-1]  # should start from 6th index (6) and start printing in reverse from there to the first character
print message[:6:-1]  # should start from the end (2) and keep printing up to 7

# changing the case of string
duplicate = message.upper()
print duplicate
print duplicate.lower()


greeting = "Hello World!"

print greeting.startswith("Hell")
print greeting.startswith("hELL")
print greeting.endswith("World!")

# splitting the string
split_greeting_list = greeting.split(" ")
print split_greeting_list
print "%s" %split_greeting_list
print split_greeting_list[0]
