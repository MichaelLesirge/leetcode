from tkinter import Tk

"""
quick little script to turn question titles into good filenames and put them on my clipboard
now also makes commit name and title after leetcode update

my code kinda sucks here but i was just righting a tiny script for myself
"""

r = Tk()
r.withdraw()

def display(s: str) -> None:
    print(s)
    r.clipboard_clear()
    r.clipboard_append(s)
    print()

def ask(prompt: str) -> str:
    v = input(prompt + ": ")
    if v.lower() == "exit":
        raise KeyboardInterrupt
    return v

def multi_input_input(prompt: str, lines: int) -> list[str]:
    print(prompt + ":")
    return [input() for i in range(lines)]

def format_desc(stats: list[str], question_name: str) -> tuple[str, str]:
    performance = f"{stats[1]}, faster than {stats[3]}"
    memory = f"{stats[5]}, less than {stats[7]}"

    return performance, f"""Runtime: {performance} of Python3 online submissions for {question_name}.\nMemory Usage: {memory} of Python3 online submissions for {question_name}."""

def main():
    print("1. URL at top of code as comment")
    print("2. Performance as commit title")
    print("3. All info as commit description")
    print()

    try:
        while True:            
            title = ask("Enter question title")
            number, question_name = title.split(".")
            filename = f"{int(number.strip()):04d}_{question_name.strip().lower().replace(" ", "_")}.py"
            display(filename)

            stats = multi_input_input("Enters stats", 12)
            
            print()
            
            display(f"Runtime: {stats[1]}{stats[2]}, faster than {stats[4]}")
            
            ask("press enter")
            
            display(rf"""
Solution for Leetcode problem #{number}.

Python3 online submission for {question_name.strip()}:
Runtime: {stats[1]}{stats[2]}, quicker than {stats[4]} of users
Memory: {stats[7]}{stats[8]}, smaller than {stats[10]} of users

https://leetcode.com/problems/""")


    except KeyboardInterrupt:
        print()
        print("Bye bye!")

        r.destroy()
        exit()

if __name__ == "__main__":
    main()
