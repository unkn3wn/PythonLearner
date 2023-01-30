def main():
    # is_even is function
    x = int(input("X? "))
    if is_even(x):
        print("even")
    else:
        print("odd")


# this is how you determine if even or odd

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False 
    
    
    
main()