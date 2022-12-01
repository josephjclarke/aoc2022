calorie_list = []
current = []

with open("input01.txt") as file:
    for line in file:
        if line == "\n":
            calorie_list.append(current)
            current = []
        else:
            current.append(int(line))
    calorie_list.append(current)

print(max(map(sum,calorie_list)))
