left_hand_list = []
right_hand_list = []

with open('input.txt', 'r') as file:
    for line in file:
        left_hand_list.append(int(line.split('   ')[0]))
        right_hand_list.append(int(line.split('   ')[1]))    

left_hand_list.sort()
right_hand_list.sort()

distance = 0
score = 0

for value_left, value_right in zip(left_hand_list, right_hand_list):
    distance = distance + abs(value_left - value_right)
    score = score + (value_left * right_hand_list.count(value_left))

print(f"The distance is: {distance}")
print(f"The score is: {score}")
