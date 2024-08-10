""" 
Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). 

A signal is provided to each wire by a gate, another wire, or some specific value. 

Each wire can only get a signal from one source, but can provide its signal to multiple destinations. 

A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: 
x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:
    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). 
"""
"""
For example, here is a simple circuit:
    123 -> x
    456 -> y
    x AND y -> d
    x OR y -> e
    x LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT x -> h
    NOT y -> i
After it is run, these are the signals on the wires:
    d: 72
    e: 507
    f: 492
    g: 114
    h: 65412
    i: 65079
    x: 123
    y: 456

What signal is ultimately provided to wire a?


&	a & b	Bitwise AND
|	a | b	Bitwise OR
~	~a	Bitwise NOT
<<	a << n	Bitwise left shift
>>	a >> n	Bitwise right shift

Part Two
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
"""

from data.d7 import input_data

test_data = [
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i"
]

values = {}
def caseing(act, signal):
    if len(act) == 1:
        try: vl = int(act[0])
        except: vl = values.get(act[0])
        if vl is not None:
            values[signal] = vl
            return True
        else: 
            return False
        
    if act[0] == 'NOT':
        try: x = int(act[1])
        except: x = values.get(act[1])
        if x is not None:
            new_vl = ~x
            values[signal] = new_vl
            return True
        else: return False
        
    try: x = int(act[0])
    except: x = values.get(act[0])
    try: y = int(act[2])
    except: y = values.get(act[2])
    
    if x == None or y == None:
        return False
    
    if act[1] == 'AND':
        new_vl = x & y
    elif act[1] == 'OR':
        new_vl = x | y
    elif act[1] == 'LSHIFT':
        new_vl = x << y
    elif act[1] == 'RSHIFT':
        new_vl = x >> y

    values[signal] = new_vl
    return True
    

def part_one():
    imp = input_data
    limp = 1
    while len(imp) > 0:
        if len(imp) == limp:
            break
        limp = len(imp)
        for command in imp:
            act, signal = command.split(' -> ')
            act = act.split(' ')
            val_assigned = caseing(act, signal)
            if val_assigned:
                imp.pop(imp.index(command))
    print(values['a']) # 3176
    return

def part_two():
    # b is no longer 44430 but instead 3176
    imp = input_data
    limp = 1
    while len(imp) > 0:
        if len(imp) == limp:
            break
        limp = len(imp)
        for command in imp:
            act, signal = command.split(' -> ')
            act = act.split(' ')
            val_assigned = caseing(act, signal)
            if val_assigned:
                imp.pop(imp.index(command))
    print(values['a']) # 14710
    return

part_one()
part_two()