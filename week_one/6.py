"""
Part One
You've decided to deploy one million lights in a 1000x1000 grid.
Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction
The lights at each corner are at 0,0, 0,999, 999,999, and 999,0. 

The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. 
Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

Set up your lights by doing the instructions Santa sent you in order.

For example:
    Turn on 0,0 through 999,999 would turn on (or leave on) every light.
    Toggle 0,0 through 999,0 would toggle the first line of 1000 lights
        turning off the ones that were on
        turning on the ones that were off
    Turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

Part Two

The light grid you bought actually has individual brightness controls.
Each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, 
to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:
    - turn on 0,0 through 0,0 would increase the total brightness by 1.
    - toggle 0,0 through 999,999 would increase the total brightness by 2000000.

"""

from data.d6 import input_data
import numpy as np

grid = np.zeros([1000,1000], dtype=int)

def trip_switch_1(coord, instruction):
    if instruction == 'on': val = 1
    elif instruction == 'off': val = 0
    else: 
        if grid[coord[0]][coord[1]] == 1 : val = 0
        else: val = 1
    grid[coord[0]][coord[1]] = val
    
def trip_switch_2(coord, instruction):
    cv = grid[coord[0]][coord[1]]
    if instruction == 'on': cv+=1
    elif instruction == 'off': cv-=1
    elif instruction == 'toggle': cv+=2 
    if cv <0: cv = 0
    grid[coord[0]][coord[1]] = cv

def part_one():
    for inst in input_data:
        inst = inst.split(' ')
        start = [int(v) for v in inst[-3].split(',')]
        end = [int(v) for v in inst[-1].split(',')]
        for y in range(end[0]-start[0]+1):
            for x in range(end[1]-start[1]+1):
                trip_switch_1([start[0]+y, start[1]+x], inst[-4])
    print(grid.sum()) # 543903
    return

def part_two():
    for inst in input_data:
        inst = inst.split(' ')
        start = [int(v) for v in inst[-3].split(',')]
        end = [int(v) for v in inst[-1].split(',')]
        for y in range(end[0]-start[0]+1):
            for x in range(end[1]-start[1]+1):
                trip_switch_2([start[0]+y, start[1]+x], inst[-4])
    print(grid.sum()) # 14687245
    return 

part_one()
part_two()