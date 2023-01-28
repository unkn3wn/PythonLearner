name = input("whats your name?").strip().title()
# splitting users name into first name and last name 
first, last = name.split(" ")


print(f"hello {last}")