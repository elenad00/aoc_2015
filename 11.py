"""
Part One:
Santa has devised a method of coming up with a password based on the previous one. 
He finds his new password by incrementing his old password repeatedly until it's valid.

Incrementing is just like counting with numbers: 
xx, xy, xz, ya, yb, and so on
Increase the rightmost letter one step; 
If it was z, it wraps to a
Repeat with the next letter to the left until one doesn't wrap around.

Unfortunately he has some additional password requirements:
    Passwords must include one >= three letter straight
        like abc, bcd, cde up to xyz. 
    Passwords may not contain the letters i, o, or l
    Passwords must contain two different, non-overlapping pairs of letters, 
        like aa, bb, or zz.

For example:
    ! hijklmmn (fails i)
    ! abbceffg (fails run)
    ! abbcegjk (fail double pair)
    abcdefgh -> abcdffaa
    ghijklmn -> ghjaabcc

Given Santa's current password (your puzzle input), what should his next password be?

Part Two:
What should Santa's next password be?
"""
import re


def test_validity(password):
    ''' check the password validity '''
    letters = ["i","o","l"]
    for letter in letters:
        if letter in password:
            return False

    matches = 0
    for p, char in enumerate(password):
        if (p<len(password)-2 and
            char == password[p+1] and char!=password[p+2]):
            matches+=1
        elif (p == len(password)-2 and
              char == password[p+1]):
            matches+=1
    
    if matches < 2:
        return False

    run = False
    for p, char in enumerate(password):
        char = ord(char)
        if p<len(password)-2 and (
            char+1 == ord(password[p+1]) and
            char+2 == ord(password[p+2])):
            run = True
    return run

def increase_input(input_data):
    ''' increase to the next password '''
    ord_string = []
    for v in input_data:
        ord_string.append(ord(v))

    for o, cv in reversed(list(enumerate(ord_string))):
        if cv<=121:
            ord_string[o]=cv+1
            break
        elif cv == 122:
            ord_string[o]=97
        elif ord_string[o+1] == 97:
            ord_string[o]=cv+1
    
    ord_string = [chr(o) for o in ord_string]
    new_input = "".join(ord_string)
    return new_input

def run_gen_new_pass(input_data):
     while True:
        valid = test_validity(input_data)
        if valid:
            print(f"Next Password: {input_data}")
            return
        input_data = increase_input(input_data)

def part_one():
    ''' part one of the day challenge '''
    input_data = "hxbxwxba"
    run_gen_new_pass(input_data) # hxbxxyzz
   
        
def part_two():
    input_data = "hxbxxzaa"
    run_gen_new_pass(input_data) # hxcaabcc

part_one()
part_two()
