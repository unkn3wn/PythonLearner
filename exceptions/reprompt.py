# this while true basically keeps running unti the user enters a number
while True:
    try:
        x = int(input("Whats x? "))
# if ww have an error we will execute this 
    except ValueError:
        print("x is not an integer")
# else if no error we will print this 
    else:
        break
print(f"x is {x}")