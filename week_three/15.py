"""
Part One
Your recipe leaves room for exactly 100 teaspoons of ingredients. 
You make a list of the ingredients you could use to finish the recipe and their properties.
You can only measure ingredients in whole-teaspoon amounts accurately,
    and you have to be accurate so you can reproduce your results in the future. 
The total score of a cookie can be found by adding up each of the properties
    (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:
    Butterscotch: 
        capacity -1, 
        durability -2, 
        flavor 6, 
        texture 3, 
        calories 8
    Cinnamon: 
        capacity 2, 
        durability 3, 
        flavor -2, 
        texture -1, 
        calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon
    would result in a cookie with the following properties:
    A capacity of 44*-1 + 56*2 
        = 68
    A durability of 44*-2 + 56*3 
        = 80
    A flavor of 44*6 + 56*-2 
        = 152
    A texture of 44*3 + 56*-1 
        = 76
Multiplying these together (68 * 80 * 152 * 76) results in a total score of 62842880,
    which happens to be the best score possible given these ingredients. 
If any properties had produced a negative total, it would have instead become zero,
    causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties
What is the total score of the highest-scoring cookie you can make?

Part Two:
Someone asks if you can make another recipe that has exactly 500 calories per cookie. 
Keep the rest of your award-winning process the same
    (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. 
The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?
"""

from functools import reduce
from operator import mul
import re
from typing import List

import numpy as np

def min_zero_sum(*ns):
    return max(0, sum(ns))

def get_cookie_ingredients():
    m = []
    regex = r"(\w+): capacity (-?\d+), durability (\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)"
    data = open("data/d15.txt").read()

    for i, c, d, f, t, cls in re.findall(regex, data):
        lst = [c, d, f, t, cls]
        m.append([int(v) for v in lst])
    m = np.array(m)
    return m

def get_scores(m) -> List:
    return [
        (
        reduce(
            mul, 
            map(
                min_zero_sum, 
                *map(mul, [i, j, k, l], m[:, :-1])
            )
        ),
        sum(
            map(
                mul,
                [i, j, k, l], m[:, -1]
            )
        ))
        for i in range(101) 
        for j in range(0, 101-i) 
        for k in range(0, 101-j-i) 
        for l in [100 - i - j - k]
    ]
    
def part_one():
    m = get_cookie_ingredients()
    scores = get_scores(m)
    print(max(s[0] for s in scores)) # 222870

def part_two():
    m = get_cookie_ingredients()
    scores = get_scores(m)
    print(max(s[0] for s in scores if s[1] == 500)) # 117936
    
part_one()
part_two()