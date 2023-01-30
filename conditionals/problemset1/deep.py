"""
In deep.py, implement a program that prompts the user 
for the answer to the Great Question of Life, the Universe and Everything, 
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. 
Otherwise output No.
"""

x = input("what is the Answer to the Great Question of Life, The Universe, and Everthing? ")

match x:
    case "42" | "Forty Two" | "forty-two" :
        print("Yes")
    case _:
        print("No")
