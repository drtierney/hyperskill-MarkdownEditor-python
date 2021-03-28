formats = ["plain", "bold", "italic",
           "header", "link", "inline-code",
           "ordered-list", "unordered-list", "new-line"]

commands = ["!help", "!done"]


def print_help():
    print("Available formatters: {0}".format(" ".join(formats)))
    print("Special commands: {0}".format(" ".join(commands)))


done = False

while not done:
    user_input = input("- Choose a formatter: ")
    if user_input == "!done":
        done = True
    elif user_input == "!help":
        print_help()
    elif user_input in formats:
        pass
    else:
        print("Unknown formatting type or command. Please try again")
