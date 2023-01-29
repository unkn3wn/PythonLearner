# float is a number with decimal point
x = float(input("whats x? "))
y = float(input("whats y? "))
# this rounds to the second digit
z = round(x / y, 2)
# this adds a comma so if you doo 500 plus 500 it will print
# 1,000 like this and not like this 1000
print(f"{z:,}")

# to round 
# round(number[, ndigits])
# ndigits is optional



# antother way to write it using f string

"""
x = float(input("what is x? "))
y = float(input("what is y? "))
z = x/y

print(f"{z:.2f}")

"""