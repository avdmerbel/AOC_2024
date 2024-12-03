# import regular expression package
import re 
# import mul and reduce function
from operator import mul
from functools import reduce

day = 3

# load input puzzle 1
input = open(f'AOC2024_day{day}_input.txt','r')
lines=input.readlines()

# define the pattern in regular expression
pattern = re.compile("mul\\([0-9]+,[0-9]+\\)")
example_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

example_result = []
for m in pattern.finditer(example_string): # find iter find the index where the pattern is found (start and end)
    example_result.append(example_string[m.start():m.end()]) # subset the string by the found start and ends
    
# get the valid muls in a list
muls = []
for line in lines:
    for m in pattern.finditer(line):
        muls.append(line[m.start():m.end()])

# get pattern for digits
numbers=re.compile('\\d+')

# see if it works
for item in example_result:
    reduce(mul, map(int, numbers.findall(item))) 
    # findall extracts all non-overlapping matches of the pattern in given string so all digits in our case
    # map applies the function int to each element of the list produced by find all (like apply in R)
    # reduce applies the mul function (multiplication) to elements of the list

# get total for the multiplications
total = 0
for item in muls:
    total += reduce(mul, map(int, numbers.findall(item)))
