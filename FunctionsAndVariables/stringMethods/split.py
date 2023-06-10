# we accepet a input from user
name = input("WHat is your name? ").strip()
# Split the input into first and last name by using the space character as the separator
# The title() method capitalizes the first character of each word
first, last = name.title().split(" ")
#print out the split of variabels but in this case we only want the first name 
print(f"hello {first}")
