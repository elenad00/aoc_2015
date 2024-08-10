# '''
# Part One
# It is common in many programming languages to provide a way to escape special characters in strings. 

# However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.

# Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are:
# - \\ (which represents a single backslash)
# - \" (which represents a lone double-quote character)
# - \x plus two hexadecimal characters (which represents a single character with that ASCII code).

# Disregarding whitespace, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

# Part Two
# Now, let's go the other way. 
# In addition to finding the number of characters of code, you should now encode each code representation as a new string and find the number of characters of the new encoded representation, including the surrounding double quotes.

# For example:
#     "" encodes to "\"\"", an increase from 2 characters to 6.
#     "abc" encodes to "\"abc\"", an increase from 5 characters to 9.
#     "aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
#     "\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.
# Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal. 

# - \\ (which represents a single backslash)
# - \" (which represents a lone double-quote character)
# - \x plus two hexadecimal characters (which represents a single character with that ASCII code).

# For example, for the strings above, 
# - the total encoded length (6 + 9 + 16 + 11 = 42) minus 
# - the characters in the original code representation (23, just like in the first part of this puzzle) is 42 - 23 = 19.
# '''

from data.d8 import input_data

test_data = [
    r'""',
    r'"abc"',
    r'"aaa\"aaa"',
    r'"\x27"'
]

def clear_hex(line):
    ind = line.index('\\x')
    line = line[0:ind]+'H'+line[ind+4:]
    return line

def stripper(line):
    line = line.replace('\\\\','/')
    while "\\x" in line:
        line = clear_hex(line)
    line = line.replace("\\\"", "'")
    line = line.replace("\"","")
    return len(line)

def adder(line):
    # \ = /, " = ^
    line = line[1:-1]
    line = line.replace('\\"','./.^')
    line = line.replace('\\x', '//x')
    line = line.replace('\\', '//')
    line = line.replace('"', '^/^')
    line = f'"/"{line}"/"'
    return len(line)
    

def part_one():
    diff_len = 0
    for line in input_data:
        diff_len+=(len(line)-stripper(line))
    print(diff_len) # 1342
    return

def part_two():
    diff_len = 0
    for line in input_data:
        diff_len+=(adder(line)-len(line))
    print(diff_len) # 2074
    return

part_one()
part_two()