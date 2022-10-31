from tkinter import Tk

"""
quick little script to turn question titles into good filenames and put them on my clipboard
"""

r = Tk()
r.withdraw()

def format_title(title: str) -> str:
    number, name = title.split(".")
    number = int(number.strip())
    name = name.strip().lower().replace(" ", "_")
    return f"{number:04d}_{name}.py"

print("1. URL at top of code as comment")
print("2. Preformance as commit title")
print("3. All info as commit descrition")
print()

try:
    while True:
        title = input("Enter question title: ")
        if title.lower() == "exit":
            raise KeyboardInterrupt

        filename = format_title(title)
        print(filename)
        r.clipboard_append(filename)

        print()

except KeyboardInterrupt:
    print()
    print("Bye bye!")

    r.destroy()
    exit()
