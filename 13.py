"""
Part One
You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. 
You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

Using the test data:
    Seat Bob next to Alice (Bob gains 83, Alice gains 54) +137 (137) 
    Seat Carol next to Bob (Carol gains 60, Bob loses 7) +53 (190)
    Seat David next to Carol (Carol gains 55, David gains 41) +96 (286)
    Seat Alice next to David (Alice loses 2, David gains 46) +44 (330)

After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?

Part Two
In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?
"""

from itertools import product
import re
from typing import Any, Dict, List
from data.d13 import input_data

def get_blank_happiness() -> List[Any]:
    names = set(l.split(' ')[0] for l in input_data)
    happiness = {}
    for x, y in product(names, names):
        if x != y:
            happiness[frozenset((y, x))] = 0
    return [names, happiness]

def generate_moods() -> List[Any]:
    names, happiness = get_blank_happiness()
    pattern = re.compile(
        '^([a-zA-Z]+) would (lose|gain) ([0-9]+) happiness units by sitting next to ([a-zA-Z]+)'
    )
    for line in input_data:
        desc = pattern.match(line)
        if not desc: 
            raise TypeError()
        first, status, measure, second = desc.groups()
        measure = int(measure)
        if status == "lose":
            measure *= -1    
        happiness[frozenset((first, second))] += measure
    return [names, happiness]

def optimize(
    remainder: set,
    current: str,
    end: str,
    happiness: Dict[frozenset, int]
) -> int:
    if len(remainder) == 0:
        return happiness[frozenset((current, end))]
    result = 0
    for next in remainder:
        result = max(
            result, happiness[frozenset((current, next))] + 
            optimize(
                remainder.difference({next}),
                next, end, happiness
            )
        )
    return result

def part_one():
    names, happiness = generate_moods()
    start = names.pop()
    answer1 = optimize(names, start, start, happiness)
    print(answer1) # 618
    return
   
        
def part_two():
    names, happiness = generate_moods()
    for name in names:
        happiness[frozenset(('me', name))] = 0
    names.add('me')
    start = names.pop()
    answer2 = optimize(names, start, start, happiness)
    print(answer2) # 601
    return

test_data = ["Alice would gain 54 happiness units by sitting next to Bob","Alice would lose 79 happiness units by sitting next to Carol","Alice would lose 2 happiness units by sitting next to David","Bob would gain 83 happiness units by sitting next to Alice","Bob would lose 7 happiness units by sitting next to Carol","Bob would lose 63 happiness units by sitting next to David","Carol would lose 62 happiness units by sitting next to Alice", "Carol would gain 60 happiness units by sitting next to Bob", "Carol would gain 55 happiness units by sitting next to David", "David would gain 46 happiness units by sitting next to Alice", "David would lose 7 happiness units by sitting next to Bob", "David would gain 41 happiness units by sitting next to Carol"]

part_one()
part_two()
