"""
Part One:
Santa needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. 
The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. 
To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:
    If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
    If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
    
Part Two:
Now find one that starts with six zeroes.
"""

from data.d4 import input_data
from _md5 import md5

def run_hex(search_val):
    v=1
    while True:
        i = f'{input_data}{v}'
        i = bytes(i, encoding='utf8')
        result=md5(i).hexdigest()
        if search_val in result[:6]:
            return v, result
        v+=1

def part_one():
    print(run_hex('00000'))
     # 117946

def part_two():
    print(run_hex('000000'))
    # 3938038

part_one()
part_two()
    
