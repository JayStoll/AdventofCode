from itertools import islice
from string import ascii_lowercase, ascii_uppercase

alphabet = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
upper_alphabet = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=27)} 

total = 0
with open("input.txt") as f:
    while True:
        next_n_lines = list(islice(f, 3))
        if not next_n_lines:
            break
        first = next_n_lines[0].replace("\n", "")
        second = next_n_lines[1].replace("\n", "")
        third = next_n_lines[2].replace("\n", "")
        common = list(set(first)&set(second)&set(third))
        for c in common:
            if c.isupper():
                total = total + int(upper_alphabet[c])
            else:
                total = total + int(alphabet[c])

print(total)