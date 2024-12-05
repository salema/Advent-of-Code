import re

result = 0
enabled = True

with open('input.txt', 'r') as file:
    memory = file.read()
    pattern = r"do\(\)|don\'t\(\)|mul\([0-9]*,[0-9]*\)"

    for instruction in re.findall(pattern, memory):
        if instruction == "do()":
            enabled = True
            print("Enabled!")
        elif instruction == "don't()":
            enabled = False
            print("Disabled!")
        else:
            if enabled:
                result += int(instruction.split(',')[0][4:]) * int(instruction.split(',')[1][:-1])
            else:
                print(f"Skipped: {instruction}")

print(f"The result is {result}")
