# import regular expression package
import re 
# import mul and reduce function
from operator import mul
from functools import reduce

day = 3

# load input puzzle 1
input = open(f'AOC2024_day{day}_input.txt','r')
lines=input.read().replace('\n','')

# define the pattern in regular expression
pattern = re.compile("mul\\(\\d+,\\d+\\)")
  
# get the valid muls in a list
muls = []
for m in pattern.finditer(lines): # find iter find the index where the pattern is found (start and end)
    muls.append(lines[m.start():m.end()]) # subset the string by the found start and ends

# get pattern for digits
numbers=re.compile('\\d+')

# get total for the multiplications
total = 0
for item in muls:
    total += reduce(mul, map(int, numbers.findall(item)))
    # findall extracts all non-overlapping matches of the pattern in given string so all digits in our case
    # map applies the function int to each element of the list produced by find all (like apply in R)
    # reduce applies the mul function (multiplication) to elements of the list

# PART 2
example_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
pattern = "mul\\(\\d+,\\d+\\)"

ignore_start = "don't\\(\\)"
ignore_end = "do\\(\\)"

ignore_range = []
for match in re.finditer(f"{ignore_start}(.*?){ignore_end}", lines, re.DOTALL):
    start = match.start()
    end = match.end()
    ignore_range.append((start, end))

matches=[]
for match in re.finditer(pattern, lines):
    is_ignored = any(start <= match.start() < end for start, end in ignore_range)
    if not is_ignored:
        matches.append(match.group())
        
total=0
for item in matches:
    total += reduce(mul, map(int, numbers.findall(item)))

# HARD CODE BECAUSE I ARE HAVE STOOPID
sum((mul(389,212),mul(210,340),mul(80,124),mul(240,258),mul(579,916),mul(584,139)))