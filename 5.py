"""
Part One
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:
    It contains at least three vowels (aeiou only).
    It contains at least one letter that appears twice in a row.
    It does not contain the strings ab, cd, pq, or xy.

How many strings are nice?

Part Two
Now, a nice string is one with all of the following properties:
- It contains a pair of any two letters that appears at least twice in the string without overlapping
- It contains at least one letter which repeats with exactly one letter between them

How many strings are nice under these new rules?
"""

from data.d5 import input_data

class TestStringsOne():
    def __init__(self, string):
        self.string = string
        self.count_vowels()
        self.check_pairs()
        self.check_for_bad_pairs()
        self.check_valid()
        
    def count_vowels(self):
        vowel_count = 0
        vowel_count+=self.string.count('a')
        vowel_count+=self.string.count('e')
        vowel_count+=self.string.count('i')
        vowel_count+=self.string.count('o')
        vowel_count+=self.string.count('u')
        self.vowel_count = vowel_count
        
    def check_pairs(self):
        self.pair = False
        st = self.string
        for i in range(len(st)-1):
            if st[i] == st[i+1]:
                self.pair=True
                return
    
    def check_for_bad_pairs(self):
        self.bad_pairs=False
        invalid = ['ab', 'cd', 'pq', 'xy']
        for v in invalid:
            if v in self.string:
                self.bad_pairs=True
                
    def check_valid(self):
        self.valid = True
        if self.vowel_count<3 or not self.pair or self.bad_pairs:
            self.valid=False

class TestStringsTwo():
    def __init__(self, string):
        self.string = string
        self.check_pairs()
        self.check_sandwich()
        self.check_valid()
        
    def check_pairs(self):
        self.pair = False
        st = self.string
        for i in range(len(st)-1):
            pair = st[i]+st[i+1]
            c = st.count(pair)
            if c>1:
                self.pair=True
    
    def check_sandwich(self):
        self.sandwich=False
        st = self.string
        for i in range(len(st)-2):
            if st[i] == st[i+2]:
                self.sandwich=True
                
    def check_valid(self):
        self.valid = False
        if self.sandwich and self.pair:
            self.valid=True


def part_one():
    valid = 0 
    for input in input_data:
        string = TestStringsOne(input)
        if string.valid:
            valid+=1
    print(valid) # 236

def part_two():
    valid = 0 
    for input in input_data:
        string = TestStringsTwo(input)
        if string.valid:
            valid+=1
    print(valid) # 51

part_one()
part_two()