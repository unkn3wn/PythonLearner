def main():
    x = int(input("X? "))
    if is_even(x):
        print("even")
    else:
        print("odd")


def is_even(n):
    return True if n % 2 == 0 else False
    # return n % 2 == 0


main()
