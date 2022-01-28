# Functions in Python are created a using the def keyword followed by the function name,
# a set of parantheses that will contain the function parameters/arguments, and instead of 
# a curly bracket as the opening and closing of the function block, Python uses the semi-colon
# to mark the opening of the function block and a colon.

# Below is a simple function that when run, will print to the command line, 'Hello World!'
def sayHi():
    print('Hello World!');
# To run a function, we use the function name followed by the parenetheses.
# Below is the sayHi function being called.
sayHi();

# Functions in Python depend a lot on indendation to show flow and relation to certain blocks.
# Below is a function with an if-else statement.
def ifElse(a):
    if(a > 18):
        print('You are an adult');
    else:
        print('You are still a kid!');
# As you can see in the function above, indentation in Python is a way code blocks are distinguished
# and how you can tell which code belongs to which block

# Below is the ifElse function running with two different arguments passed
ifElse(24); # Will print 'You are an adult'
ifElse(16); # Will print 'You are still a kid!'