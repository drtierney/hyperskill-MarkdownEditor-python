formats = ["plain", "bold", "italic",
           "header", "link", "inline-code",
           "ordered-list", "unordered-list", "new-line"]

commands = ["!help", "!done"]

lines = []


def print_help():
    print("Available formatters: {0}".format(" ".join(formats)))
    print("Special commands: {0}".format(" ".join(commands)))


def print_lines():
    print("".join(lines))


def plain_format(txt):
    global lines
    lines.append(txt)


def bold_format(txt):
    global lines
    lines.append("**{0}**".format(txt))


def italic_format(txt):
    global lines
    lines.append("*{0}*".format(txt))


def inline_code_format(txt):
    global lines
    lines.append("`{0}`".format(txt))


def link_format(lbl, link):
    global lines
    lines.append("[{0}]({1})".format(lbl, link))


def header_format(lvl, txt):
    global lines
    lines.append("{0} {1}\n".format("#" * lvl, txt))


def new_line_format():
    global lines
    lines.append("\n")


def ordered_list_format():
    pass


def unordered_list_format():
    pass


done = False

while not done:
    command = input("- Choose a formatter: ")
    if command == "!done":
        done = True
    elif command == "!help":
        print_help()
    elif command in formats:
        if command == "plain":
            text = input("- Text: ")
            plain_format(text)
        if command == "bold":
            text = input("- Text: ")
            bold_format(text)
        if command == "italic":
            text = input("- Text: ")
            italic_format(text)
        if command == "inline-code":
            text = input("- Text: ")
            inline_code_format(text)
        if command == "link":
            label = input("Label: ")
            url = input("URL: ")
            link_format(label, url)
        if command == "header":
            level = int(input("Level: "))
            while not (level > 1 or not (level < 6)):
                print("The level should be within the range of 1 to 6")
                level = int(input("Level: "))
            text = input("- Text: ")
            header_format(level, text)
        if command == "new-line":
            new_line_format()
        if command == "ordered-list":
            pass
        if command == "unordered-list":
            pass
        print_lines()
    else:
        print("Unknown formatting type or command. Please try again")
