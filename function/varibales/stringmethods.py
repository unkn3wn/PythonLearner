# strip removes any white space
# title makes each other word capitlize
name = input("whats your name?").strip().title()
"""
name = name.strip().title()

or

name = name.strip()

name = name.title()

these all do the same thing as line 3
"""
print(f"hello {name}")