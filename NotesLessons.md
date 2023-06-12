### What is a text Editor ?

    program to write text

### What is a CLI ?

    Command Line Interface

    to run a program in the terminal you have to run "python FILENAME.py"


### assignment
 * "=" means assigning

### Integers

* int function

    ```Python
    x = input("x = ")
    y = input("y = ")
    z = int(x) + int(y)
    print(z)
    ```
* either one of these works the same thing 
    ```Python
    x = int(input("x"))
    y = int(input("y"))
    z= x + y
    print(z)
    ```

* this is how you turn strings into integers by using the "int" function

### float

* a numer that has a decimal point in it
* this is the 3rd type of data python takes

      ```Python
    x = input("x = ")
    y = input("y = ")
    z = float(x) + float(y)
    print(z)
    ```

* you can also round the result to the nearest integer 

    ```Python
    x = input("x = ")
    y = input("y = ")
    z = float(x) + float(y)
    print(z)
    ```
##### round(number[,ndigits])
###### EXAMPLE OF HOW TO USE
    ```Python
    x = input("x = ")
    y = input("y = ")
    z = round(float(x) + float(y))
    print(z)
    ```

* INPUT: x = 4.234, y = 3.345
* OUTPUT: z = 8
* sense we are rounding to the nearest integer it will round up because 4.234 + 3.345 = 7.579 and that round it is 8

###### this is how you round to the nearest digit

    ```Python
    x = input("x = ")
    y = input("y = ")
    z = round(float(x)+float(y), 2)
    print(z)
    ```

* by adding this int , 2 to the end it will round to the nearest hundredth