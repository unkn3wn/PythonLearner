## Variables and Types

* Dont need to declare varibles before using them, nor the type

## Numbers

* Python supports 2 types of numbers intergers (ex: 1) and floats (Ex: 0.3)

* defining a Integer in Python:

        ```Python
         int = 7
         print(int)
        ```

* definind a float point number

        ```Python
        float = 7.0
        print(float)
        ```

        ```Python
        myFloat = float(7)
        print(myFloat)
        ```

# String Methods

### str.capitalize()

    ```Python
    name = input("Whats your name? ")
    print(name.capitlize())
    ```

* this will return the first character Capitlized

* say for example you input "asd" it will print "Asd"

### str.upper()

* makes all characters upperCase

    ```Python
    name = input("what is your name).upper();
    print(name)
    ```
* this example if we input "asd" we will get a output of "ASD" all the characters will turn uppercase

### str.casefold()

* converts string into lower case

    ```Python
    name = input("what is your name? ").upper()
    print(name.casefold())
    ```

* we input "asd" first it will convert it into "ASD" all upper because at the end of our input function we have .upper so there  foward it converts it to upper but once we print we will get a output of "asd" because it converts it back to lowercase 

### str.encode()
* its a specfic method used to conver text or strings into a format computers can understand

* if no encode is applied by default it will use UTF8 (unicode Transformation Format-8 bit)

For Example 

1. using ASCII (American Standard Code For Information Interchange)


    ```Python
    txt = "Hello"
    encoded = txt.encode("ascii")
    print(encoded)
    ```
* OUTPUT:  `b'Hello'

* Explanation: when we call .encode("ascii") it converts the string "Hello" into ASCII in this case "Hello" is within the range of ASCII. 