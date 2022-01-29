# As we know in computing/programming, booleans are binary variables, that have two 
# possible values called “true” and “false”. Booleans are very useful with flow control in
# programming using flow-control statements.

# In Python, you can assign true or false as values for a variable as so
isTrue = True;
isFalse = False;

# Like many other programming languages, Python also takes advantage of comparison operators
# to respond to comparisons with boolean values. Below is a list of comparsion operators used in Python
# --------------------------------------------------- #
# == -> Equal to
# != -> Not equal to
# < -> Less than
# > -> Greater than
# <= -> Less than or equal to
# >= -> Greater than or equal to
# --------------------------------------------------- #

# Python does not have a strict equality comparison operator like JavaScript or Java
# Below is a sample of using the above comparison
def isGreater(val):
    if(val > 10):
        return True;
    else:
        return False;
isGreater(12);
# The above function will take an argument and compare to see if it is greater than 10

def isEqual(val):
    if(val == 10):
        return True;
    else:
        return False;
isEqual(10);
# The above function will take an argument and compare to see if its equal to 10

def isLess(val):
    if(val != 10):
        return True;
    else:
        return False;
isLess(10);
# The above function will take an argument and compare to see if its less than 10