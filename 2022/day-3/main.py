from string import ascii_lowercase, ascii_uppercase

alphabet = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
upper_alphabet = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=27)} 

total = 0

with open("input.txt") as file:
    lines = file.readlines()

    for line in lines:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        common = list(set(firstpart)&set(secondpart))
        for c in common:
            if c.isupper():
                total = total + int(upper_alphabet[c])
            else:
                total = total + int(alphabet[c])

print(total)