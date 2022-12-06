data = open("input06.txt").read().rstrip()

for i in range(4, len(data)):
    if len(set(data[i - 4:i])) == 4:
        print(i)
        break
for i in range(14, len(data)):
    if len(set(data[i - 14:i])) == 14:
        print(i)
        break
