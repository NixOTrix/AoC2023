import re
file1 = open("./puzzle.txt", 'r')
lines = file1.readlines()

allnums = []

for line in lines:
    first = re.findall(r'\d+', line)[0]
    last = re.findall(r'(\d+)(?!.*\d)', line)[0]
    number = first[0] + last[-1]
    allnums.append(int(number))
    
total = 0
for number in allnums:
    total += number
print(total)