import re

# our stacks array
stacks = []
with open("input.txt") as file:
    input = file.readlines()
    for col in range(0, len(input[0])):
        stacks.append("")
        for line in range(0,8):
            # we don't care about the "[]" part of the equation
            if input[line][col] not in ["[", "]", " "]:
                stacks[col] += input[line][col]

stacks = [stack for stack in stacks if stack != ''][:-1]

# start looking at the file from the 10th line moving into an array or arrays
# each inner arry will be [MOVE, FROM, WHERE]
instructions = [[int(d) for d in re.findall(r"\d+", line.strip())] for line in input[10:]]

for instruction in instructions:
    amount_to_move = instruction[0]
    from_stack = stacks[instruction[1] - 1]
    where = stacks[instruction[2] - 1]

    temp = from_stack[:amount_to_move]
    stacks[instruction[1] - 1] = from_stack[amount_to_move:]

    stacks[instruction[2] - 1] = temp + where

print("".join([stack[0] for stack in stacks]))
