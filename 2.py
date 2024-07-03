"""
Part One:
They have a list of the dimensions (length l, width w, and height h) of each 
present, and only want to order exactly as much as they need.

Find the surface area of each box, which is 2*l*w + 2*w*h + 2*h*l.
The elves also need a little extra paper for each present: the area of the smallest side.

How many total square ft of wrapping paper should they order?

Part Two:
The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. 
Each present also requires a bow made out of ribbon as well; 
    the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. 
    Don't ask how they tie the bow, though; they'll never tell.

For example:
    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present 
    plus 2*3*4 = 24 feet of ribbon for the bow, 
    for a total of 34 feet.
    
    A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present 
    plus 1*1*10 = 10 feet of ribbon for the bow, 
    for a total of 14 feet.
    
How many total feet of ribbon should they order?
"""

from data.d2 import input_data

new_input = []
for i in input_data:
    new_input.append(i.split('x'))


def part_one():
    total = 0
    for present in new_input:
        l, w, h = [int(p) for p in present]
        area = [(l*w),(w*h),(h*l)]
        minimum = sorted(area)[0]
        a = sum([a*2 for a in area])
        total+=(a+minimum)
    print(total) # 1606483
    

def part_two():
    total= 0
    for present in new_input:
        l, w, h = sorted([int(p) for p in present])
        total+=((l*2+w*2)+(l*w*h))
    print(total) # 3842356
    

part_one()
part_two()

