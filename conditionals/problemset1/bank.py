x = input(str("Greeting: ")).title()

match x:
    case "Hello" | "Hello, Newman":
        print("$0")
    case "How you doing?":
        print("$20")
    case "What's happening?":
        print("$100")