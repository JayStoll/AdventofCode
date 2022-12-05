total = 0

with open("input.txt") as file:
    lines = file.readlines()
    
    for line in lines:
        inputs = line.split(",")

        first = inputs[0].split("-")
        second = inputs[1].replace("\n", "").split("-")

        first_set = set(range(int(first[0]), int(first[1])+1))
        second_set = set(range(int(second[0]), int(second[1])+1))

        if (not first_set.isdisjoint(second_set) or  not second_set.isdisjoint(first_set)):
            total = total + 1

print(total)