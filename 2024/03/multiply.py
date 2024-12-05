import re

result = 0

with open('input.txt', 'r') as file:
    memory = file.read()
    pattern = r"mul\([0-9]*,[0-9]*\)"

    for instruction in re.findall(pattern, memory):
        print(instruction)
        result += int(instruction.split(',')[0][4:]) * int(instruction.split(',')[1][:-1])

print(f"The result is {result}")
