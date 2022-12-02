highest_calorie = 0

with open("input.txt") as f:
    lines = f.readlines()

    total = 0
    for line in lines:
        line = line.replace('\n', '')
        if not line:
            highest_calorie = highest_calorie if highest_calorie > total else total
            total = 0
        else:
            total = total + int(line)
            

print(highest_calorie)
