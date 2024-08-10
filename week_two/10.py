"""
Part One:
Today, the Elves are playing a game called look-and-say. 
They take turns making sequences by reading aloud the previous sequence
and using that reading as the next sequence. 
For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, 
using the previous value as input for the next step. 
For each step, 
take the previous value
replace each run of digits (like 111) with 
the number of digits (3)
followed by the digit itself (1).

For example:

1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).

Starting with the digits in your puzzle input, apply this process 40 times. 
What is the length of the result?

Part Two:
Neat, right? You might also enjoy hearing John Conway talking about this sequence, Conway's Game of Life.

Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?
"""

def cycle_through(times, input_data):
    i = 0
    while i < times:
        cv = input_data[0]
        count = 0
        new_num = ''
        for v, value in enumerate(input_data):
            if value==cv:
                count+=1
            else:
                new_num+=(str(count)+cv)
                count=1
                cv=value
        i+=1
        new_num+=(str(count)+cv)
        input_data=new_num
    return input_data

def part_one():
    ''' part one of the days challenge '''
    input_data = '3113322113'
    new_num = cycle_through(40, input_data)
    print(len(new_num)) # 329356

def part_two():
    ''' part two of the days challenge '''
    input_data = '3113322113'
    new_num = cycle_through(50, input_data)
    print(len(new_num)) # 4666278
    
part_one()
part_two()