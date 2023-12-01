import re
file1 = open("./puzzle.txt", 'r')
lines = file1.readlines()

num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '0': '0'
}


allnums = []

for line in lines:
    tempfirst_dict = {}
    templast_dict = {}
    for num_word in num_dict:
        pos = line.find(num_word)
        tempfirst_dict[num_word] = pos
        pos = line.rfind(num_word)
        templast_dict[num_word] = pos

    tempfirst_dict = {key:val for key, val in tempfirst_dict.items() if val != -1}
    templast_dict = {key:val for key, val in templast_dict.items() if val != -1}
    if len(tempfirst_dict) == 0 and len(templast_dict) == 0:
        continue
    last = max(templast_dict, key=templast_dict.get)
    first = min(tempfirst_dict, key=tempfirst_dict.get)
    last_num = num_dict[last]
    first_num = num_dict[first]
    number = first_num + last_num
    print(line)
    print(number)
    allnums.append(int(number))
    
total = 0
for number in allnums:
    total += number
print(total)