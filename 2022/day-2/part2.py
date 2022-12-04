"""
Create a weight table
0 - lost
the same number - tie
4 - win
"""
opponent_list = {
    "A": [1, [1, 0, 4]], # rock
    "B": [2, [0, 2, 4]], # paper
    "C": [3, [0, 4, 3]]  # scissors
}

check_list = {
    "X": 1, # need to lose # rock
    "Y": 2, # need to tie  # paper
    "Z": 3  # need to win  # scissors
}

total = []
def add_to_total(add, incr):
    return add + incr 

# open the file
with open("input.txt") as file:
    # break the curent line into a list based on an empty string
    lines = file.readlines()
    for line in lines:
        x = line.split()

        inc = 0
        idx = 0

        opponent_list_chart = opponent_list[x[0]][1]

        if x[1] == "X": # lose
            idx = opponent_list_chart.index(0)
            inc = 0
        elif x[1] == "Y": # tie
            idx = opponent_list_chart.index(opponent_list[x[0]][0])
            inc = 3
        else: # win
            idx = opponent_list_chart.index(4)
            inc = 6

        total.append(
            add_to_total(check_list[list(check_list.keys())[idx]], inc)
        )

print(sum(total))