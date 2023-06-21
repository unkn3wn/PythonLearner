def main():
    num = get_number()
    hello(num)
    
def get_number():
    while True:
        n = int(input("what is N? "))
        if n > 0:
            break
    return n
    
def hello(n):
    
    for _ in range(n):
        print("hello")
    
main()