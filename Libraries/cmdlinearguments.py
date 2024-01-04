# sys.argv = this is a list
import sys
# on cmd line type file name you want to run after you type in name 

# if you want to put your full name you have to put double quotes 
try: 
        if len(sys.argv) <2:
            print("Too few arugments")
        elif len(sys.argv) > 2:
            print("to many arguments")
        else:
            print("Hello", sys.argv[1])
except IndexError as e:
    print(f"errro is {e}")
    