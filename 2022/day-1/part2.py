highest_calorie = 0
second = 0
third = 0

with open("input.txt") as f:
    lines = f.readlines()

    total = 0
    for line in lines:
        line = line.replace('\n', '')
        if not line:
            if total > highest_calorie:
                temp = highest_calorie
                temp1 = second
                highest_calorie = total
                second = temp
                third = temp1
            elif total > second:
                temp = second
                second = total
                third = temp
            elif total > third:
                third = total
            total = 0
        else:
            total = total + int(line)
            

print(highest_calorie+ second + third)
