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


def output_lines():
    file = open("output.md", "w")
    file.writelines(lines)
    file.close()


def plain_format(txt):
    return txt


def bold_format(txt):
    return "**{0}**".format(txt)


def italic_format(txt):
    return "*{0}*".format(txt)


def inline_code_format(txt):
    return "`{0}`".format(txt)


def link_format(lbl, link):
    return "[{0}]({1})".format(lbl, link)


def header_format(lvl, txt):
    return "{0} {1}\n".format("#" * lvl, txt)


def new_line_format():
    return "\n"


def list_format(items, ordered=False):
    return [f"* {item}\n" for item in items] if not ordered \
        else [f"{index + 1}. {item}\n" for index, item in enumerate(items)]


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
            lines.append(plain_format(text))
        if command == "bold":
            text = input("- Text: ")
            lines.append(bold_format(text))
        if command == "italic":
            text = input("- Text: ")
            lines.append(italic_format(text))
        if command == "inline-code":
            text = input("- Text: ")
            lines.append(inline_code_format(text))
        if command == "link":
            label = input("Label: ")
            url = input("URL: ")
            lines.append(link_format(label, url))
        if command == "header":
            level = int(input("Level: "))
            while not (level >= 1 or not (level <= 6)):
                print("The level should be within the range of 1 to 6")
                level = int(input("Level: "))
            text = input("- Text: ")
            lines.append(header_format(level, text))
        if command == "new-line":
            lines.append(new_line_format())
        if command.endswith("-list"):
            row_count = int(input("Number of rows: "))
            while not row_count > 0:
                print("The number of rows should be greater than zero")
                row_count = int(input("Number of rows: "))
            rows_input = [input(f"Row #{n + 1}: ") for n in range(row_count)]
            lines.extend(list_format(rows_input, True) if command.startswith("ordered") else list_format(rows_input))
        print_lines()
    else:
        print("Unknown formatting type or command. Please try again")

output_lines()
