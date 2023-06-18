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

## String Methods

### str.capitalize()

* makes first character capitalized

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

* we input "asd" first it will convert it into "ASD" all upper because at the end of our input function we have .upper so there foward it converts it to upper but once we print we will get a output of "asd" because it converts it back to lowercase

### str.encode()

* its a specfic method used to conver text or strings into a format computers can understand

* if no encode is applied by default it will use UTF8 (unicode Transformation Format-8 bit)

> For Example

1. ASCII (American Standard Code For Information Interchange)

   ```Python
   txt = "Hello"
   encoded = txt.encode("ascii")
   print(encoded)
   ```

* OUTPUT: `b'Hello'

* Explanation: when we call .encode("ascii") it converts the string "Hello" into ASCII in this case "Hello" is within the range of ASCII.

2. UTF-8

* the number 8 stands for bits

  ```Python
  txt = "こんにちは"
  encoded = txt.encode("utf-8")
  print(encoded)
  ```

* OUPUT: b'\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf'
* Explantion: the string here is in Japense ("こんにちは" = "Hello"). We are calling "utf\*8" which results in it giving us hexadecimal values

* NOTE UTF\*8 is compatible with ASCII

3. UTF-16

* the number 16 stands for bits

  ```Python
  txt = "😊"
  encoded = txt.encode("utf-16")
  print(encoded)
  ```

* OUTPUT: b'\xff\xfe\x3a\xd8\x3c\xde'
* Explanation: We have a emoji "😊", calling utf-16 converts the string into utf-16, It uses variable length encoding, uses 2 bytes also 16 bits for most of the characters, also returns hexadecimals

4. UTF-32

* the number 32 stands for bits

  ```Python
  txt = "Hello"
  encoded = txt.encode("utf-32")
  print(encoded)
  ```

* OUTPUT: b'\xff\xfe\x00\x00H\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00'

* In this example, we have the same string "Hello". When we call encode("utf-32"), it converts the string into UTF-32 encoding. UTF-32 uses a fixed-length encoding of 4 bytes (32 bits) for each character, regardless of the character's actual representation. The resulting byte string contains hexadecimal values representing the encoded characters.

5. ISO-8859-1 (Latin-1)

* schema that can represent characters used in Western Europ languages It's a superset of ASCII and includes characters such as accented letters.

    ```Python
    txt = "é"
    encoded = txt.encode("iso-8859-1")
    print(encoded)
    ```
* OUTPUT:b'\xe9
 * Explanation: In this example, we have a string with an accented letter, "é". When we call encode("iso-8859-1"), it converts the string into ISO-8859-1 encoding. ISO-8859-1 is an 8-bit encoding that can represent characters used in Western European languages. The resulting byte string contains a single byte representing the encoded character.


 ### str.strip()

 * Gets rid of any white spaces in your code 

  ``` Python
  name  = input("Whats your name? ").strip()
  print(f"hello, {name}")
  ```

* INPUT: "      JEFF JEFF"
* OUTPUT: "HELLO JEFF JEFF"

* in this example it got rid of all the white spacing before jeff


### str.split()

* splits string at certain seperator

  ```Python
  name = input("Whats your name? ").title()

  first, last = name.split(" ")

  print(f"Hello, {first}")
  ```
* INPUT : "CHAPO GUZMAN" 
* OUTPUT "Hello Chapo" 


## Conditionals

### Matimatical questions 

* Equals: a == b
* Not Equals: a != b
* Less than: a < b
* Less than or equal to: a <= b
* Greater than: a > b
* Greater than or equal to: a >= b

#### if statements
* example of a if statement
    ```Python
    x = int(input("What X? "))
    y = int(input("Whats Y? "))
    if x < y:
        print("x is less than y")
    ```


* if true it will print the mesage

#### elif statements

    ```Python
    age = int(input("age? "))
    if age < 18:
        print("you are underage")
    elif age >= 18:
        print("you are old of age") 
    ```

### Loops 

* reapting something over and over until particular condition is satisfied
### while loop

  ```Python
  # we have a variable of x we set it equal to zero
  i = 0 
  # while statement x < 3 we will print you dont know me son after each iteration we will add 1 to x so after 3 more iterations the statement will no longer be true so it stops.(remember we count from zero 0,1,2)
  while i < 3 :
    i = i + 1
    print("You dont know me son")
  ```
 