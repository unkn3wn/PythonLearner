def main():
    height = int(input("square height: "))
    print_square(height)
    
def print_square(size):
    for i in range(size):
        print("#" *size)

main()