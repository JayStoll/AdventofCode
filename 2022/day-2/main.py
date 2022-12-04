opponent_list = {
    "A": 1, # rock
    "B": 2, # paper
    "C": 3  # scissors
}

"""
Create a weight table
0 - lost
the same number - tie
4 - win
"""
my_list = {
    "X": [1, [1, 0, 4]], # rock
    "Y": [2, [4, 2, 0]], # paper 
    "Z": [3, [0, 4, 3]]  #scissors
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
        
        current = list(opponent_list.keys())
        current_index = current.index(x[0])
        
        inc = 0

        if opponent_list[x[0]] < my_list[x[1]][1][current_index]:
            inc = 6
        elif opponent_list[x[0]] > my_list[x[1]][1][current_index]:
            inc = 0
        else:
            inc = 3

        total.append(add_to_total(my_list[x[1]][0], inc))




print(sum(total))