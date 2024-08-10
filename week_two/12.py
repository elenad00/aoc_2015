"""
Part One:
Santa needs help balancing the books after a recent order. 
Unfortunately, their accounting software uses a peculiar storage format. 
That's where you come in.

They have a JSON document which contains a variety of things: 
    arrays ([1,2,3]), 
    objects ({"a":1, "b":2}), 
    numbers 
    strings
Your first job is to simply find all of the numbers throughout the document and add them together.

For example:
    [1,2,3] and {"a":2,"b":4} both have a total_val of 6.
    [[[3]]] and {"a":{"b":4},"c":-1} both have a total_val of 3.
    {"a":[-1,1]} and [-1,{"a":1}] both have a total_val of 0.
    [] and {} both have a total_val of 0.
You will not encounter any strings containing numbers.

What is the total_val of all numbers in the document?

Part Two:
Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

[1,2,3] still has a sum of 6.
[1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
{"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
[1,"red",5] has a sum of 6, because "red" in an array has no effect.
"""

# from data.d12 import input_data
                           
import json
from typing import Any, Dict

f = open('data/d12.json')
input_data = json.load(f)

def cycle(v: Any, second: bool) -> int:
    total_val = 0
    if type(v) is int:
        total_val+=v
    elif type(v) is list:
        for value in v:
            total_val+=cycle(value, second)
    elif type(v) is dict:
        lv=list(v.values())
        if not (second and "red" in lv):
            total_val+=cycle(lv, second)
    return total_val

def part_one():
    total_val = 0
    for key in input_data:
        total_val+=cycle(input_data[key], False)
    print(total_val) 

def part_two():
    total_val = 0
    for key in input_data:
        total_val+=cycle(input_data[key], True)
    print(total_val)


part_one() # 119433
part_two() # 68466