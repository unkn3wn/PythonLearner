# float is a number with decimal point
x = float(input("whats x? "))
y = float(input("whats y? "))

z = round(x+y)

# this adds a comma so if you doo 500 plus 500 it will print
# 1,000 like this and not like this 1000
print(f"{z:,}")

# to round 
# round(number[, ndigits])
# ndigits is optional
