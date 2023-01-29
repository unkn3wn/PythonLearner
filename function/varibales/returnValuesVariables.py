# these are comments 
# input allows a user to type something in the terminal. 
# what ever input we get from the user will be set to name
# name = input("whats your name?")
# # we than get what is stored in the variable and attach it to hello
# print("hello, "+ name)


# more on return values
def main():
    x = int(input("First num"))
    print("squared", square(x))
    
    
def square(n):
    return n * n
    # pow(n,2)
    # n * 2
main()