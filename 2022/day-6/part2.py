line = ""
with open("input.txt") as file:
    line = file.readline()

# position we want to start and stop at
start_line = 0
end_line = 14
TARGET = 14

while end_line <= len(line):
    group_letters = line[start_line:end_line:1]
    start_line += 1
    end_line += 1

    if len(set(group_letters)) == TARGET:
        print(end_line - 1)
        break