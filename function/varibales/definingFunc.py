# this is a function 
# lines 3 4 are a funtion that takes in a parameter as input
def hello(to="world"):
    print("hello", to)
    
name = input("whats your name? ")

# this one will print out hello world/ reason for being
# is due to our parameter to is set equal to world 
hello()
# while this one will print out hello what ever user inputs 
hello(name)