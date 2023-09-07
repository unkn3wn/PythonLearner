# we are going to try this
try:
    x = int(input("Whats x? "))
# if ww have an error we will execute this 
except ValueError:
    print("x is not an integer")
# else if no error we will print this 
else:
    print(f"x is {x}")