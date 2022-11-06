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

def format_title(title: str) -> tuple[str, str]:
	number, q_name = title.split(".")
	q_name = q_name.strip()
	number = number.strip()
	number = int(number)
	name = q_name.lower().replace(" ", "_")
	return f"{number:04d}_{name}.py", q_name

def format_desc(stats: list[str], question_name: str) -> tuple[str, str]:
	preformance = f"{stats[1]}, faster than {stats[3]}"
	memory = f"{stats[5]}, less than {stats[7]}"

	return preformance, f"""
Runtime: {preformance} of Python3 online submissions for {question_name}.
Memory Usage: {memory} of Python3 online submissions for {question_name}.
"""

def main():
	print("1. URL at top of code as comment")
	print("2. Preformance as commit title")
	print("3. All info as commit description")
	print()

	try:
		while True:
			title = ask("Enter question title")
			filename, name = format_title(title)
			display(filename)

			stats = multi_input_input("Enters stats", 8)
			commit_name, commit_desc = format_desc(stats, question_name=name)
			display(commit_name)
			ask("press enter")
			display(commit_desc)


	except KeyboardInterrupt:
		print()
		print("Bye bye!")

		r.destroy()
		exit()

if __name__ == "__main__":
	main()
