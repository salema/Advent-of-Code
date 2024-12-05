safe = 0
safe_with_dampener = 0

def is_linear(report: list) -> bool:
    result = True

    for index, value in enumerate(report):
        if index < len(report) - 1:
            if (report[0] < report[1]):        
                result &= value < report[index + 1]
            elif (report[0] > report[1]):
                result &= value > report[index + 1]
            else:
                result &= False

    return result


def are_diffs_small(report: list) -> bool:
    result = True

    for index, value in enumerate(report):
        if index < len(report) - 1:
            result &= 1 <= abs(value - report[index + 1]) <= 3

    return result 

def is_safe_report(report: list) -> bool:    
    return is_linear(report) and are_diffs_small(report)

def is_safe_report_with_dampener(report: list) -> bool:
    safe = False

    for index in range(len(report)):
        short_report = report.copy()
        short_report.pop(index)
        safe |= is_linear(short_report) and are_diffs_small(short_report)

    return safe

with open('input.txt', 'r') as file:
    for line in file:
        report = [int(value) for value in line.split()]
    
        if is_safe_report(report):
            safe += 1
        if is_safe_report_with_dampener(report):
            safe_with_dampener += 1

print(f"There are {safe} safe reports!")
print(f"There are {safe_with_dampener} safe reports with dampener!")
