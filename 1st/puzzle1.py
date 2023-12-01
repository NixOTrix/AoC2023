# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
# Consider your entire calibration document. What is the sum of all of the calibration values?

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