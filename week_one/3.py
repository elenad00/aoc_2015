"""
Part One:
Santa is delivering presents to a 2D grid of houses.

He begins by delivering a present to the house at his starting location.
Moves are always exactly one house to the n(^), s(v), e(>), or w(<). 
He delivers a present to the house at his new location.
Santa ends up visiting some houses more than once. 

How many houses receive at least one present?  
"""
"""
Part Two:
Santa and Robo-Santa start at the same location (delivering two presents to the same starting house)
They take turns moving based on instructions from the elf.

How many houses receive at least one present?

For example:
    ^v = 3 houses
    ^>v< = 3 houses
    ^v^v^v^v^v = 11 houses
"""

from data.d3 import input_data

class Move():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.coords = [[0,0]]
        return
        
    def move(self, char):
        if char == '^': self.y+=1
        elif char == 'v': self.y-=1
        elif char == '>': self.x+=1
        else: self.x-=1
        
        if [self.x, self.y] not in self.coords:
            self.coords.append([self.x,self.y])
            
def part_one():
    santa = Move()
    for char in input_data:
        santa.move(char)
    print(len(santa.coords)) # 2572

def part_two():
    santa = Move()
    robot = Move()
    i=0
    while i < len(input_data):
        santa.move(input_data[i])
        robot.move(input_data[i+1])
        if i+2<=len(input_data): i+=2
        else: break
    concat = santa.coords + robot.coords
    nl = []
    for coords in concat:
        if coords not in nl: nl.append(coords)
    print(len(nl)) # 2631


part_one()
part_two()
