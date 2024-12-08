day = 5

# get the input
input = open(f'AOC2024_day{day}_input.txt','r')
#input = open(f'example_day5.txt', 'r')
lines=input.readlines()

# find where the rules end and updates start
cut = lines.index('\n')

# prepare data
# get rules and updates in a tuple (ordered and unchangeable)
rules_base = []
updates_base = []

for line in lines[0:cut]:
    rules_base.append(line.split())
for line in lines[cut+1:len(lines)]:
    updates_base.append(line.split())

rules = []
for rule in rules_base:
    rules.append(tuple(map(int, rule[0].split('|'))))
    
updates = []
for update in updates_base:
    updates.append(tuple(map(int, update[0].split(','))))
    
def check_rule(update, rules):
    # get indices from the update 
    # check orders in the rules

    invalid_elements = 0

    for index, value in enumerate(update):
        
        number_in_after_rule =[]
        number_in_before_rule=[]
        indices_after=[]
        indices_before=[]

        # first find all rules where the current number should be first
        number_first = [rule for rule in rules if rule[0]==value]
        
        # find all rules where the current number should come after some other number
        number_last = [rule for rule in rules if rule[1]==value]
        
        # find all numbers that are both in the after rule and in the update
        # so which numbers should always come after the current number
        number_in_after_rule = [number for number in update[:index] + update[index+1:] if number in [after[1] for after in number_first]]

        # find all numbers that are both in the before rule and in the update
        # so number have to come before the current number
        number_in_before_rule = [number for number in update[:index] + update[index+1:] if number in [before[0] for before in number_last]]

        # get the indices of all matching numbers in the tuple
        indices_after = [i for i, value in enumerate(update) if value in number_in_after_rule if number_in_after_rule]
        indices_before = [i for i, value in enumerate(update) if value in number_in_before_rule if number_in_before_rule]
        
        
        if (indices_after and index > max(indices_after)) or (indices_before and index < max(indices_before)):
            invalid_elements += 1
     
    return invalid_elements

count=[]
for update in updates:  
    count.append(check_rule(update=update, rules=rules))
        
indices = []
for index, value in enumerate(count):
    if value == 0:
        indices.append(index)

def find_middle(update):
    return update[(len(update)-1)//2]

relevant_updates = []
for index in indices:
    relevant_updates.append(updates[index])

middle_values = 0
count = 0
for update in relevant_updates:
    middle_values += find_middle(update)
    count += 1

# part 2
