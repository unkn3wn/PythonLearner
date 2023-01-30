# this is like a switch

name = input("what is your name? ")

match name:
    case "Ferni" |"fer" |"Fer":
        print("LH")
    case "Jeff" | "jef":
        print("jH")
    case _:
        print("who?")
