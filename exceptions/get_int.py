# Define the main function
def main():
    # Step 8: Retrieve an integer using the get_int function
    x = get_int()
    
    # Step 9: Print the value of x
    print(f"x is {x}")

# Define a function named get_int
def get_int():
    # Step 2: Use a while loop to continuously prompt for input
    while True:
        try:
            # Step 4: Ask the user for input and attempt to convert it to an integer
            x = int(input("X? "))
        except ValueError:
            # Step 5: Handle the exception when the input is not an integer
            print("X is not an integer")
        else:
            # Step 6: If no exception occurs, break out of the loop
            break
    
    # Step 7: Return the valid integer value
    return x

# Call the main function to start the program
main()
