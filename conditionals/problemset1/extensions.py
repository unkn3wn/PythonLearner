file_name = input("File name: ")

match file_name:
    case "cat.gif":
        print("image/gif")
    case "cat.jpeg":
        print("image/jpeg")
    case "cat":
        print("application/octet-stream")