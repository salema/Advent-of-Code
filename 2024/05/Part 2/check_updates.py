
def calc_correct_updates_sum(rules_file: str, updates_file: str) -> int:
    rules = []
    with open(rules_file, 'r') as file:
        for line in file:
            rule = line.split('|')
            rules.append((int(rule[0]), int(rule[1][:-1])))

    updates = []
    with open(updates_file, 'r') as file:
        for line in file:
            updates.append([int(value) for value in line.split(',')])
    
    sum = 0
    for update in updates:
        is_fine = True
        for rule in rules:
            is_fine &= (rule[0] not in update or rule[1] not in update) or update.index(rule[0]) < update.index(rule[1])
        
        print(f"{update} valid? {is_fine}")
        if is_fine:
            sum += update[int(len(update) / 2 - .5)]

    return sum

assert(calc_correct_updates_sum('sample_rules.txt', 'sample_updates.txt') == 143)
print(f"Printer sum: {calc_correct_updates_sum('rules.txt', 'updates.txt')}")
