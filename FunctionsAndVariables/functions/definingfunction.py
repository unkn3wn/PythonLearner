# We have a function that takes in the user's name.
# By default, if no name is passed, it will print "Hello, world."
# For example, in line 13, if no argument is provided, "world" will be used as the default name.

def hello(name="world"):
    # We print out their name.
    print("Hello,", name)


# We prompt the user to enter their name and store it in the variable 'name'.
name = input("What's your name? ")

# We call the 'hello' function and pass in the 'name' variable.
hello(name)

# We call the 'hello' function without passing any arguments.
# It will use the default name "world" and print "Hello, world."
hello()
