# This is the code for the 3rd module

def calc_footage(length = int(input('What is the width?')), width = int(input('What is the width?'))):
    # length = input('What is the length?')
    # width = input('What is the width?')
    footage = length * width
    print('The total square footage is',footage)
# calc_footage(int(input('What is the length?')),int(input('What is the width?')))


def calc_circumference(diameter):
    # diameter = input('What is the diameter?')
    from math import pi
    circumference = pi * diameter
    print('The circumference is:',circumference)
# calc_circumference(int(input('What is the diameter?')))
