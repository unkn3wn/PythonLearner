name = input("whats your name?")
"""
The end paramater in the print function is used to add any string at the end 
of the output of print statement. for example here we use end so instead of 
making a new line it will take the print from line 10 and join it together 
with the print in hello 9 so it will out "Hello, name".
"""
print("hello, " ,end="")
print(name)

# result is "hello, name"
# instead od
# hello
# name