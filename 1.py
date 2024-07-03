"""

Part One: 
Santa starts on floor 0 and  follows the instructions one char at a time.
( means he should go up one floor
) means he should go down one floor.
He will never find the top or bottom floors.

To what floor do the instructions take Santa?

Part Two:
Find the position of the first character that causes him to enter floor -1. 
The first character in the instructions = pos 1, and so on.

What is the position of the character that causes Santa to first enter the basement?
"""

from data.d1 import input_data

def part_one():
    up = input_data.count('(')
    down = input_data.count(')')
    floor = up-down
    print(floor) # 232

def part_two():
    floor = 0
    for i in range(len(input_data)):
        if input_data[i] == '(': floor+=1
        else: floor-=1
        if floor == -1:
            print(i+1) # 1783
            exit()

part_one()
part_two()