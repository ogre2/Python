# In Python, variables are created the moment you assign a value to it
# Python does not have any preceding keywords to the variable name, none that identify
# the data type being stored (string, number, etc.) that is. Variables are created with
# their name followed by the assignment operator and the subsequent variable.

# Here is a string variable
mystr = 'Cool beans';

# Here is a number variable
num = 44;

# Using the print() function that Python has, we can print the values of the variables
# into the command line
print(mystr); # This will print to the command line 'Cooll beans'
print(num); # This will print 44 to the command line

# Casting is available in Python, this will enable you to specify data types assigned to variables

# String casting
a = str(3); # a will be '3'
# Integer casting
b = int(4); # b will be the number 4
# Decimal/float casting
c = float(8); # c will be decimal number 8.0

# You can get the type of a variable using Python's type() function
print(type(a)); # This will print <class 'str'> identifying that the variable/data is a string
print(type(b)); # This will print <class 'int'> identifying that the variable/data is an integer
print(type(c)); # This will print <class 'float'> identifying that the variable/data is a float

# **NOTE**
# Strings in Python, like most other programming languages, can be declared by either double or single quotes
x = 'A string';
# The above is the same as below
x = "A string";

# Case sensitibity
# Capitalization of variable names does make a difference, meaning, variable named str is not the same
# as a variable named Str or STR
STR = 'Yo!';
# the above is not the same variable as
Str = 'Hi!';

# Meaning, Str will not overwrite STR

# Python also allows you to assign multiple values to multiple variables
h, i, j = "Python", "Is", "Cool";
print(h); # This will print "Python"
print(i); # This will print "Is"
print(j); # This will print "Cool"

# You can also assign the same value to multiple variables, example below.
c = d = e = "Apples";
print(c); # This will print "Apples"
print(d); # This will print "Apples"
print(e); # This will print "Apples"
